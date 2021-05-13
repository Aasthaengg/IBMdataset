import sys
sys.setrecursionlimit(10**9)
N,M=map(int,input().split())
G=[[] for i in range(N)]
a,b=0,0
for i in range(M):
  a,b=map(int,input().split())
  G[b-1].append(a-1)
DP=[-1]*N
def f(x):
  if DP[x]!=-1:
    return DP[x]
  DP[x]=0
  for i in range(len(G[x])):
    DP[x]=max(DP[x],f(G[x][i])+1)
  return DP[x]

for i in range(N):
  f(i)
print(max(DP))