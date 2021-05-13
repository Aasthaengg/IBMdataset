N = int(input())
X = [[] for i in range(N)]
for i in range(N):
  A = int(input())
  for j in range(A):
    X[i].append(list(map(int, input().split())))
ans = 0
for s in range(1 << N):
  #1:TRUE, 0:UNKNOWN
  state = [(s >> j) & 1 for j in range(N)]
  f = 0
  for i in range(N):
    if state[i] == 0:
      continue
    for x in X[i]:
      if state[x[0]-1] != x[1]:
        f = 1
        break
    if f == 1:
      break
  if f == 0:
    ans = max(ans, sum(state))
print(ans)