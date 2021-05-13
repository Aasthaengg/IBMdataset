from itertools import permutations
N,M,R = map(int,input().split())
r = list(map(int,input().split()))
for i in range(R):
  r[i] -= 1
g = [[10 ** 8] * N for i in range(N)]
for i in range(M):
  A,B,C = map(int,input().split())
  A -= 1 
  B -= 1
  g[A][B] = C
  g[B][A] = C
def warchall_floyd(n):
  for i in range(n):
    #経由する頂点
    for j in range(n):
      #始点
      for k in range(n):
        #終点
        g[j][k] = min(g[j][k],g[j][i]+g[i][k])
        
warchall_floyd(N)
ans = float('inf')
for i in permutations(r):
  now = 0
  for j in range(R-1):
    now += g[i[j]][i[j+1]]
  if now < ans:
    ans = now
print(ans)
