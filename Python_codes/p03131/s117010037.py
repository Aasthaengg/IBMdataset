k, a, b = map(int, input().split())

if k < a:
    ans = k + 1

else:
    if b <= a + 2:
        ans = k + 1

    else:
        k -= a - 1
        q, r = divmod(k, 2)
        ans = a + q * (b - a) + r

print(ans)
