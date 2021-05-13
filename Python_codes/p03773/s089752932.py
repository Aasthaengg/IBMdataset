a, b = map(int, input().split())
ans = a + b if a + b <= 23 else a + b - 24
print(ans)