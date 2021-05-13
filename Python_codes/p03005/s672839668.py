def solve(n, k):
    return n - k if k > 1 else 0

n, k = map(int, input().split())
print(solve(n, k))