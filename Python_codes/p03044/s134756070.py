import sys

sys.setrecursionlimit(10**6)

n = int(input())
if n == 1:
    print(1)
else:
    edge=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v,w = map(int,input().split())
        edge[u-1].append((v-1,w%2))
        edge[v-1].append((u-1,w%2))
 
    color =[-1]*n
    def dfs(node,edge):
        for next_node,w in edge[node]:
            if color[next_node] != -1:
                continue
            if w == 1:
                color[next_node] = color[node]^1
            elif w == 0:
                color[next_node] = color[node]
            dfs(next_node,edge)
        
        
    color[0] = 0
    dfs(0,edge)
    print(*color,sep="\n")