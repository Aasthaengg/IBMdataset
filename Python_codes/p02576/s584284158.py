def solve(n, x, t):
    return (n + x - 1) // x * t

n, x, t = map(int, input().split())
print(solve(n, x, t))
