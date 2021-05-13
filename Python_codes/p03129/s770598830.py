def solve(n, k):
    return "YES" if (2*k-1 <= n) else "NO"

n, k = map(int, input().split())
print(solve(n, k))