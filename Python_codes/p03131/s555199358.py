k, a, b = map(int, input().split())

if a + 2 < b:
    ans = a
    k -= a - 1
    if k%2 == 1:
        ans += 1
        k -= 1
    ans += (b - a) * (k // 2)
    print(ans)
else:
    print(k+1)