def solve(n, m):
    return abs(n * m - 2 * n - 2 * (m - 2))

_n, _m = map(int, input().split())
print(solve(_n, _m))
