a, b, c, k = map(int, input().split())

ans = 0
if k < a:
    ans = k
else:
    ans += a
    k = k - a
    if k < b:
        ans = ans
    else:
        ans = ans
        k = k - b
        if k < c:
            ans -= k
        else:
            ans = a - c

print(ans)