x, y = [int(x) for x in input().split()]

if x == 0:
    ans = abs(y) + (y < 0)
else:
    ans = 1 if (x < 0 and abs(x) < abs(y)) or (x > 0 and abs(x) > abs(y)) else 0
    ans += abs(abs(y) - abs(x))
    ans += 1 if (-1 if (x < 0 and abs(x) < abs(y)) or (x > 0 and abs(x) > abs(y)) else 1) * x * y < 0 else 0

print(ans)
