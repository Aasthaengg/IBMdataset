N, K = map(int, input().split())
T = [[] for i in range(N)]
MOD = 10 ** 9 + 7
for i in range(N - 1):
    a,  b = map(int, input().split())
    a, b = a - 1, b - 1
    T[a].append(b)
    T[b].append(a)


# 階乗 & 逆元計算
factorial = [1]
inverse = [1]
for i in range(1, K + 2):
    factorial.append(factorial[-1] * i % MOD)
    inverse.append(pow(factorial[-1], MOD - 2, MOD))


# 組み合わせ計算
def nPr(n, r):
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] * factorial[r] % MOD


ans = K
stack = [[0, 0]]  # [頂点番号, 深さ]
visited = [False] * N
while stack:
    n, depth = stack.pop()
    visited[n] = True

    child = 0
    for to in T[n]:
        if visited[to]:
            continue

        child += 1
        stack.append([to, depth + 1])

    if depth == 0:
        ans *= nPr(K - 1, child)
    else:
        ans *= nPr(K - 2, child)
    ans %= MOD

print(ans % MOD)
