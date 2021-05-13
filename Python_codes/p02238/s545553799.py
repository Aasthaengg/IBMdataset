n = int(input())
g = [[] for i in range(n)]
for i in range(n):
    g[i] = list(map(lambda x:int(x)-1,input().split()))[2:]

def dfs(v,t):
    t += 1
    d[v] = t
    for i in g[v]:
        if d[i]==-1:
            t = dfs(i,t)
    t += 1
    f[v] = t
    return t

t = 0
d = [-1]*n
f = [-1]*n

for i in range(n):
    if d[i]==-1:
        t = dfs(i,t)

for i in range(n):
    print(i+1,d[i],f[i])
