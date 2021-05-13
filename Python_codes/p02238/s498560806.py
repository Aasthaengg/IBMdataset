n = int(input())
G = [[] for i in range(n+1)] #G(i): 頂点iと隣接する頂点のlist
for i in range(n):
    a = [int(i) for i in input().split()]
    G[a[0]] = a[2:]
    G[a[0]].sort()

d = [0] * (n+1)
f = [0] * (n+1)

seen = [0] * (n+1) #頂点iが訪問済みの場合 seen[i] = 1
t = 0

def dfs(s):
    global t
    seen[s] = 1
    d[s] = t
    for i in G[s]:
        if seen[i] == 0:
            t += 1
            dfs(i)
    t += 1
    f[s] = t

for i in range(1, n+1):
    if not seen[i]:
        t += 1
        dfs(i)

for i in range(1, n+1):
    print(i, d[i], f[i])
