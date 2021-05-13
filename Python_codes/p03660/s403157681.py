import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
n=int(input())
edges=[[] for _ in range(n)]
dist=[0]*n
for i in range(n-1):
  u,v=map(int,input().split())
  u-=1
  v-=1
  edges[u].append(v)
  edges[v].append(u)
dist=[ [0]*n for _ in range(2)]
#do a dfs
def dfs(u,p,idd):#u=curr , p=par
  for nei in edges[u]:
    if nei==p:
      continue
    dist[idd][nei]=1+dist[idd][u]
    dfs(nei,u,idd)
dist[0][0]=0
dfs(0,0,0)
dist[1][n-1]=0
dfs(n-1,n-1,1)
cnt_f=cnt_s=0
for i in range(n):
  if dist[0][i]<=dist[1][i]:
    cnt_f+=1
  else:
    cnt_s+=1
print("Fennec") if cnt_f>cnt_s else print("Snuke")

