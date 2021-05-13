n, a, b = map(int, input().split())
ans = max(0, (b - a) * (n - 2) + 1)
print(ans)