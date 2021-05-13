def solve(n, m):
    return m // 2 if 2 * n >= m else (2 * n + m) // 4

_n, _m = map(int, input().split())
print(solve(_n, _m))