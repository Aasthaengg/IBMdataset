n, m = map(int, input().split())
a = sum(map(int, input().split()))
print([n - a, -1][n < a])