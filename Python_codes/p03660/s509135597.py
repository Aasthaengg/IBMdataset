import sys
sys.setrecursionlimit(2 * 10 ** 5)

n = int(input())
edge = [tuple(map(int, input().split())) for _ in range(n-1)]
connect = [set() for _ in range(n)]
for a, b in edge:
    connect[a-1].add(b-1)
    connect[b-1].add(a-1)

d1 = [0] * n
dn = [0] * n

def dfs(v, ng, dis, d):
    d[v] = dis
    ng.add(v)
    for n in connect[v]:
        if n not in ng:
            dfs(n, ng, dis+1, d)

dfs(0, set(), 0, d1)
dfs(n-1, set(), 0, dn)

black = 0
white = 0
for i in range(n):
    if d1[i] <= dn[i]:
        black += 1
    else:
        white += 1
if black > white:
    print('Fennec')
else:
    print('Snuke')