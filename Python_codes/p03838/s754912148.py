x, y = map(int, input().split())

num = abs(y) - abs(x)

if num == 0:
    ans = 1
elif num > 0:
    if x >= 0 and y >= 0:
        ans = num
    elif x < 0 and y < 0:
        ans = num + 2
    else:
        ans = num + 1
elif num < 0:
    if x > 0 and y > 0:
        ans = -num + 2
    elif x <= 0 and y <= 0:
        ans = -num
    else:
        ans = -num + 1
print(ans)