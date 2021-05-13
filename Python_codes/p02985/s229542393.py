n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
mod = 10 ** 9 + 7


def p(x, y):
    ret = 1
    for i in range(y):
        ret *= x - i
        ret %= mod

    return ret


adj = [[] for _ in range(n)]
for a, b in ab:
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)


def dfs(s):
    d = [-1] * n
    d[s] = 0
    child = [0] * n
    stack = [s]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if d[v] == -1:
                child[u] += 1
                d[v] = d[u] + 1
                stack.append(v)

    return child


c = dfs(0)
ans = 1
for i, e in enumerate(c):
    if i == 0:
        ans *= k * p(k - 1, e)
    else:
        ans *= p(k - 2, e)

    ans %= mod

print(ans)
