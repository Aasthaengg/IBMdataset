x, y = map(int, input().split())

diff = abs(abs(x)-abs(y))
bs = abs(y) - abs(x)
if x == 0 or y == 0:
    reverse = 0
else:
    reverse = 1


if x >= 0 and y >= 0:
    if bs >= 0:
        ans = diff
    else:
        ans = reverse + diff + 1
elif x >= 0 and y <= 0:
    if bs >= 0:
        ans = diff + 1
    else:
        ans = reverse + diff
elif x <= 0 and y >= 0:
    if bs >= 0:
        ans = reverse + diff
    else:
        ans = diff + reverse
elif x <=0 and y <=0:
    if bs >= 0:
        ans = reverse + diff + 1
    else:
        ans = diff
print(ans)