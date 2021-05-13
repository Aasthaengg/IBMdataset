x, y = map(int, input().split())
ax, ay = abs(x), abs(y)
ans = 0
if x >= 0:
    if y > 0:
        if x > y:
            x *= -1
            ans += 1
            ans += (-y) - x
            ans += 1
        else:
            ans += y - x
    else:
        ans += abs(ax - ay) + 1
else:
    if y > 0:
        if ax > ay:
            ans += ax - ay
            ans += 1
        else:
            ans += 1
            x *= -1
            ans += y - x
    else:
        if ay <= ax:
            ans += ax - ay
        else:
            ans += 1
            x *= -1
            ans += ay - ax
            ans += 1
print(ans)
