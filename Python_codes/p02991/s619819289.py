from collections import deque


def inpl():
    return list(map(int, input().split()))


N, M = inpl()
UV = [inpl() for i in range(M)]
S, T = inpl()
S -= 1
T -= 1

ans = [[-1, -1, -1] for i in range(N)]

uv = [[] for i in range(N)]
for u, v in UV:
    u -= 1
    v -= 1
    uv[u].append(v)

ans[S][0] = 0
que = deque()
que.append((S, 0))
t = 0
while que:
    v, t = que.popleft()
    nt = (t + 1) % 3
    for nv in uv[v]:
        if ans[nv][nt] != -1:
            continue
        elif nv == T and nt == 0:
            ans[nv][nt] = (ans[v][t] + 1) // 3
            break
        ans[nv][nt] = ans[v][t] + 1
        que.append((nv, nt))

print(ans[T][0])
