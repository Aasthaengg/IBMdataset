n = int(input())
d = [0]*n
f = [0]*n
G = [[] for _ in range(n)]
for _ in range(n):
    l = list(map(int, input().split()))
    u, k = l[:2]
    l = list(map(lambda x: x-1, l[2:]))
    G[u-1] = l

timestamp = [i+1 for i in range(2*n)]
def dfs(node):
    global d,f,G,timestamp
    if d[node]>0:
        return False
    d[node] = timestamp.pop(0)
    for v in G[node]:
        dfs(v)
    if f[node]==0:
        f[node] = timestamp.pop(0)
    return True
for i in range(n):
    dfs(i)
    
for i in range(n):
    print(i+1, d[i], f[i])
