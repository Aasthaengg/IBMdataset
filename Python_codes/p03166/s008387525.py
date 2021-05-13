import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    x,y = map(int,input().split())
    edge[x-1].append(y-1)


d = [0] * n

def dfs(v,edge):
    depth = 0
    for next_v in edge[v]:
        if d[next_v] == 0:
            depth = max(depth,dfs(next_v,edge))
        depth = max(depth,d[next_v])
    depth += 1 
    d[v] = depth
    return depth

for i in range(n):
    dfs(i,edge)
print(max(d)-1)