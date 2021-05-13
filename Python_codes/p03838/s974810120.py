x, y = map(int, input().split())
if y*x < 0:
    ans = abs(x + y) + 1
elif y*x == 0:
    if x < y:
        ans = y - x
    else:
        ans = x - y + 1
else:
    if x < y:
        ans = y - x
    else:
        ans = x - y + 2

print(ans)