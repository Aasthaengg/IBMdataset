import sys
sys.setrecursionlimit(1000000)

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

def dfs(v,d,dist):
    dist[v] = d
    for ve in edge[v]:
        if dist[ve] is None:
            dist = dfs(ve, d+1, dist)
    return dist
    
    
f_dist = dfs(0,0,[None]*n)
s_dist = dfs(n-1,0,[None]*n)

fget = sum(1 for f,s in zip(f_dist,s_dist) if f<=s)
print("Fennec" if fget*2>n else "Snuke")