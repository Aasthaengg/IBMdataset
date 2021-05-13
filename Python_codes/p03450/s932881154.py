import sys
sys.setrecursionlimit(10 ** 6)


def dfs(p):
    result = True
    for np, D in edge[p]:
        if pos[np] is None:
            pos[np] = pos[p] + D
            result &= dfs(np)
        else:
            if pos[p] + D != pos[np]:
                result &= False
    return result


N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for q in sys.stdin.readlines():
    L, R, D = map(int, q.split())
    L -= 1; R -= 1
    edge[L].append((R, D))
    edge[R].append((L, -D))

pos = [None] * N
result = True
for i in range(N):
    if pos[i] is None:
        pos[i] = 0
        result &= dfs(i)

ans = 'Yes' if result else 'No'
print(ans)
