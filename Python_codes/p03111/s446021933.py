N, A, B, C, *X = map(int, open(0).read().split())

def dfs(i, a, b, c):
    if i == N:
        if a * b * c == 0:
            return 10 ** 9 + 7
        return abs(A - a) + abs(B - b) + abs(C - c)

    v0 = dfs(i + 1, a, b, c)
    v1 = dfs(i + 1, a + X[i], b, c) + int(a > 0) * 10
    v2 = dfs(i + 1, a, b + X[i], c) + int(b > 0) * 10
    v3 = dfs(i + 1, a, b, c + X[i]) + int(c > 0) * 10

    return min(v0, v1, v2, v3)


print(dfs(0, 0, 0, 0))
