import heapq

N = int(input())
dic = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
  a,b,c = map(int, input().split())
  dic[a].append([b,c])
  dic[b].append([a,c])

Q, K = map(int, input().split())
memo = [float('inf')]*(N+1)
memo[K] = 0
h = [(0,K)]
while h:
  t = heapq.heappop(h)
  if t[0] > memo[t[1]]:
    continue
  for k in dic[t[1]]:
    if memo[k[0]] > t[0] + k[1]:
      memo[k[0]] = t[0] + k[1]
      heapq.heappush(h, (memo[k[0]], k[0]))
      
for _ in range(Q):
  x, y = map(int, input().split())
  print(memo[x]+memo[y])