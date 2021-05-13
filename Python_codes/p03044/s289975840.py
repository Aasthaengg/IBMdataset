import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(d, v, p):
    if (d & 1):
        C[v] = 1
    for w, u in E[v]:
        if u == p:
            continue
        dfs(d ^ w, u, v)

N = int(input())
C = [0] * N
E = [[] for _ in range(N)]
for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    E[u].append((w % 2, v))
    E[v].append((w % 2, u))
dfs(0, 0, -1)
print(*C, sep='\n')