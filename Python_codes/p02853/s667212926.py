X, Y = map(int, input().split())
ans = max(4 - X, 0) + max(4 - Y, 0) + max(12 - (X + Y) * 4, 0)
print(ans * 100000)
