n, m = map(int, input().split())
ans = abs(n * m - (4 + (n - 2) * 2 + (m - 2) * 2))
print(ans)