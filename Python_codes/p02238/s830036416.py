n = int(input())
M = [[0]*n for _ in range(n)]
st = [0]*n
d = [0]*n
f = [0]*n
tt = 0

def dfs(u,t):
    st[u] = 1
    t += 1
    d[u] = t
    for v in range(n):
        if M[u][v] == 0: continue
        if st[v] == 0: t = dfs(v,t)
    st[u] = 2
    t += 1
    f[u] = t
    return t

for _ in range(n):
    i = [int(i) for i in input().split()]
    u = i[0]
    k = i[1]
    V = i[2:]
    for v in V: M[u-1][v-1] = 1

for i in range(n):
    if st[i] == 0: tt = dfs(i,tt)

for i in range(n): print(i+1,d[i],f[i])
