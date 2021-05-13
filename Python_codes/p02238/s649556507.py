N = 100
WHITE = 0
GRAY = 1
BLACK = 2

d = [-1] * N
f = [-1] * N

def dfs_visit(n, u, tt, color):
    global d
    global f
    color[u] = GRAY
    tt += 1
    d[u] = tt
    for v in range(n):
        if M[u][v] == 0:
            continue
        if color[v] == WHITE:
            tt = dfs_visit(n, v, tt, color)
    color[u] = BLACK
    tt += 1
    f[u] = tt
    return tt

def dfs(n):
    global d
    global f
    color = []
    for u in range(n):
        color.append(WHITE)
    tt = 0

    for u in range(n):
        if color[u] == WHITE:
            tt = dfs_visit(n, u, tt, color)
    
    for u in range(n):
        print(u+1, d[u], f[u])

n = int(input())

M = [[0] * n for _ in range(n)]

for i in range(n):
    I = list(map(int, input().split()))
    u = I[0] - 1
    k = I[1]
    for j in range(k):
        v = I[j+2] - 1
        M[u][v] = 1

#print(M)

dfs(n)
