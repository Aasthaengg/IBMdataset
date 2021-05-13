
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

res = [0, 0]
cnt = [0]


def dfs(x):
    if len(x) == N:
        if all(u == v for u, v in zip(P, x)):
            res[0] = cnt[0]
        if all(u == v for u, v in zip(Q, x)):
            res[1] = cnt[0]
        cnt[0] += 1
        return

    for i in range(1, N + 1):
        if i not in x:
            x.append(i)
            dfs(x)
            x.pop()


dfs([])
print(abs(res[0] - res[1]))
