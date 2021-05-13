x, y = [int(w) for w in input().split()]

d = abs(abs(x) - abs(y))


if d == 0:
    if x - y == 0:
        ans = 0
    else:
        ans = 1
elif y == 0:
    if x < 0:
        ans = abs(x)
    else:
        ans = x + 1
else:
    ans = d

    if x * y > 0:
        if x > y:
            ans += 2
    else:
        if x > y:
            ans += 1
        elif x < 0:
            ans += 1

print(ans)
