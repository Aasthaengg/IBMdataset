import sys
sys.setrecursionlimit(100000000)

def dfs(node,distance):
  for next_node,edge_distangce in G[node]:
    if ans[next_node]==-1:
      ans[next_node]=(distance+edge_distangce)%2
      dfs(next_node,distance+edge_distangce)

n=int(input())
G=[[] for _ in range(n)]

for i in range(n-1):
  u,v,w = map(int,input().split())
  G[u-1].append([v-1,w])
  G[v-1].append([u-1,w])

ans = [-1]*n
dfs(0,0)
print(*ans,sep='\n')
