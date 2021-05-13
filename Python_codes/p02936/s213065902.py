import sys
sys.setrecursionlimit(1000000)
N, Q = map(int, input().split())
rl = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    rl[a].append(b)
    rl[b].append(a)
cnt = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x

def dfs(v, pv):
    for next_v in rl[v]:
        if next_v == pv:
            continue
        cnt[next_v] += cnt[v]
        dfs(next_v, v)
dfs(0, -1)
print(*cnt)