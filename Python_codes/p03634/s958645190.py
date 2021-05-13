import sys
input=sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
n=int(input())
edges=[[] for i in range(n)]
dis=[-1]*n
for _ in range(n-1):
  a,s,d=map(int,input().split())
  a-=1;s-=1
  edges[a].append((s,d))
  edges[s].append((a,d))
q,k=map(int,input().split())
dis[k-1]=0
def dfs(now):
  for i,d in edges[now]:
    if dis[i]==-1:
      dis[i]=dis[now]+d
      dfs(i)
dfs(k-1)
for _ in range(q):
  a,s=map(int,input().split())
  print(dis[a-1]+dis[s-1])