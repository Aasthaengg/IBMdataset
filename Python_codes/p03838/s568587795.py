x, y = map(int, input().split())

ans = None

if x < 0:
    if y < x:
        ans = x - y + 2
    elif y <= 0:  # x <= y < 0
        ans = y - x
    else:
        ans = max(abs(x), abs(y)) - min(abs(x), abs(y)) + 1
elif x == 0:
    if y < x:
        ans = x - y + 1
    else:
        ans = y - x
else:
    if y >= x:
        ans = y - x
    elif x > y > 0:
        ans = x - y + 2
    elif y == 0:
        ans = x - y + 1
    else:
        ans = max(abs(x), abs(y)) - min(abs(x), abs(y)) + 1

print(ans)