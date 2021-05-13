from itertools import permutations

def warshall_floyd(A, INF=10**20):
    d = [[INF for i in range(len(A))] for j in range(len(A))]
    for i in range(len(A)):
        d[i][i] = 0
        for j in A[i].keys():
          d[i][j] = A[i][j]

    for k in range(len(A)):
        for i in range(len(A)):
            for j in range(len(A)):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    
    return d
  
N,M,R=map(int,input().split())
r = list(map(int,input().split()))
r2 = []
for i in range(len(r)):
  r2.append(r[i]-1)
r = r2
G=[{} for _ in range(N)]
for i in range(M):
  a,b,c=map(int,input().split())
  a -= 1
  b -= 1
  G[a][b] = G[b][a] = c

d = warshall_floyd(G)

if R==2:
  print(d[r[0]][r[1]])
  exit()
  
ans = 10**20
for p in permutations(r):
  dist=0
  for i in range(R-1):
    dist += d[p[i]][p[i+1]]
  ans = min(ans,dist)
  
print(ans)