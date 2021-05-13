k, a, b = map(int, input().split())

if b - a <= 2:
    print(k + 1)
else:
    tmp = (k - a + 1) // 2
    ans = a + (b - a) * tmp
    if (k - a + 1) % 2 == 1:
        ans += 1
    print(ans)
