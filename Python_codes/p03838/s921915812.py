x, y = map(int, input().split())
if x == y:
    ans = 0
elif x == 0 and y != 0:
    if y < 0:
        ans = -y + 1
    else:
        ans = y
elif x != 0 and y == 0:
    if x < 0:
        ans = -x
    else:
        ans = x + 1
elif x < y:
    if x < 0 < y:
        if y < abs(x):
            ans = min(y - x, abs(x) - y + 1)
        else:
            ans = y + x + 1
    else:
        ans = y - x
else:
    if y < 0 < x:
        if x < abs(y):
            ans = -(y + x) + 1
        else:
            ans = y + x + 1
    elif 0 < y < x:
        ans = y + x
    else:
        ans = -(y - x) + 2

print(ans)