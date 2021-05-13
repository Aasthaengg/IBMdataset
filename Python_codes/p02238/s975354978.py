n = int(input())
M = [[0]*n for _ in range(n)]

for _ in range(n):
    u, k, *V = map(int, input().split())
    if k == 0:
        continue
    else:
        for v in V:
            M[u-1][v-1] = 1

color = ['White']*n

time = 0
d = [0]*n
f = [0]*n
def dfs_visit(u=0):
    global time
    color[u] = 'Gray'
    time += 1
    d[u] = time
    for v in range(n):
        if M[u][v] == 0:
            continue
        if color[v] == 'White':
            dfs_visit(v)
    color[u] = "Black"
    time += 1
    f[u] = time

def dfs():
    for u in range(n):
        if color[u] == 'White':
            dfs_visit(u)
    for u in range(n):
        print('{} {} {}'.format(u+1, d[u], f[u]))


dfs()
