x, y = map(int, input().split())

ans = 0

if x >= 0 and y >= 0:
    if y >= x:
        ans = y - x
    else:
        ans = abs(y-x) + 2
elif x >= 0 and y < 0:
    ans = abs(abs(y)-abs(x)) + 1

elif x < 0 and y >= 0:
    ans = abs(abs(y)-abs(x)) + 1

else:
    if y >= x:
        ans = abs(y-x)
    else:
        ans = abs(y-x) + 2

if y == 0:
    ans -= 1

print(ans)