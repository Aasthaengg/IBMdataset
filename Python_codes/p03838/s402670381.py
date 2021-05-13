x, y = map(int, input().split())

if abs(x) < abs(y):
    ans = abs(y)-abs(x)
    if x < 0:
        ans += 1
    if y < 0:
        ans += 1
    print(ans)
else:
    ans = abs(x)-abs(y)
    if 0 < x:
        ans += 1
    if 0 < y:
        ans += 1
    print(ans)
