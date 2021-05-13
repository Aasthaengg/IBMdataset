k, a, b = map(int, input().split())


if b - a < 2:
    print(k + 1)
else:
    t = k - a + 1
    if t >= 2 and t % 2 == 0:
        ans = (b - a) * (t // 2) + a
    else:
        ans = (b - a) * (t // 2) + a + 1
    print(ans)