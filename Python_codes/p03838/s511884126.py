x, y = map(int, input().split())
ans = 0
if abs(x) == abs(y):
    ans = 1
elif abs(x) < abs(y):
    ans = abs(y) - abs(x)
    if y < 0:
        ans += 1
    if x < 0:
        ans += 1
else:
    if y == 0:
        ans = abs(x) + abs(y)
    else:
        ans = abs(x) - abs(y)
    if x > 0:
        ans += 1
    if y > 0:
        ans += 1

print(ans)
