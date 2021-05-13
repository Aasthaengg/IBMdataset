a, b = map(int, input().split())
ans = (b - a) * (b - a - 1) / 2 - a
print(int(ans))
