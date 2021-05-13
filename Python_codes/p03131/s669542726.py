k, a, b = map(int, input().split())
kk = k
ans = 0
if a >= b:
    ans += k+1
else:
    if k <= a:
        ans += k+1
    else:
        ans += a
        k -= a - 1
        if k % 2 == 1:
            ans += 1
            k -= 1
        ans += (k // 2)*(b - a)


        ans = max(ans, kk+1)

print(int(ans))
