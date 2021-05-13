a, b = list(map(int, input().split()))
ans = a + b if a + b < 24 else a + b - 24
print(ans)
