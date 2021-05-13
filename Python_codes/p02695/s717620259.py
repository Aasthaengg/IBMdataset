
N, M, Q = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(Q)]


def dfs(x):
    if len(x) == N + 1:
        res = 0
        for a, b, c, d in X:
            if x[b] - x[a] == c:
                res += d
        return res

    res = 0
    for n in range(x[-1], M + 1):
        x.append(n)
        res = max(res, dfs(x))
        x.pop()
    return res


print(dfs([1]))
