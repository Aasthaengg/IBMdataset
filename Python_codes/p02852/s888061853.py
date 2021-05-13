from heapq import heappush, heappop
N, M = map(int, input().split())
s = input()
q = [(0,N)]
INF = 10**9
dic = {}
for i in range(N-1, -1, -1):
  cnt, j = q[0]
  while j-i>M:
    heappop(q)
    cnt, j = q[0]
  heappush(q, (cnt,j))
  cnt += 1 if s[i]!='1' else INF
  heappush(q, (cnt,i))
  dic[i] = j

if cnt>=INF:
  print(-1)
else:
  x = 0
  while x!=N:
    y = dic[x]
    print(y-x)
    x = y