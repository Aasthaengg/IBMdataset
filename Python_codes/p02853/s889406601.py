x, y = map(int, (input().split()))
ans = 0

ans = 300000 if x == 1 else (200000 if x == 2 else (100000 if x == 3 else 0))
ans += 300000 if y == 1 else (200000 if y == 2 else (100000 if y == 3 else 0))
ans += 400000 if x == 1 and y == 1 else 0


print(ans)
