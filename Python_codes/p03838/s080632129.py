x, y = map(int, input().split())
ans = 0
if x * y >= 0:
    if x > y:
        ans = x - y + 2
        if x * y == 0:
            ans = x - y + 1
    else:
        ans = abs(y - x)
else:
    ans = abs(abs(x) - abs(y)) + 1
print(ans)