from collections import deque

N = int(input())
m = N*(N-1) // 2

hash_table = [[0]*N for i in range(N)]
count = 0
for i in range(N):
  for j in range(i+1, N):
    hash_table[i][j] = hash_table[j][i] = count
    count += 1


graph = [[] for i in range(m)]
before_this = [0] * m
for i in range(1, N+1):
  A = deque(list(map(int, input().split())))
  pre_a = A.popleft()
  pre_pair = hash_table[i-1][pre_a-1]
  for a in A:
    pair = hash_table[i-1][a-1]
    graph[pre_pair].append(pair)
    before_this[pair] += 1
    pre_pair = pair


games = deque([])
for i in range(m):
  if not before_this[i]:
    games.append(i)


if not games:
  ans = -1
else:
  ans = 0
  num_finished = 0
  while games:
    ans += 1
    num_games = len(games)
    num_finished += num_games
    for i in range(num_games):
      pair = games.popleft()
      subseq = graph[pair]
      for ss in subseq:
        before_this[ss] -= 1
        if not before_this[ss]:
          games.append(ss)
    
  if num_finished != m:
    ans = -1

print(ans)