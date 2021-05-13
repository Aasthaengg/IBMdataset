k, a, b = map(int, input().split())

if a + 2 >= b:
    print(k + 1)
elif k <= a - 1:
    print(k + 1)
else:
    remain = k - (a - 1)
    d, m = divmod(remain, 2)
    ans = a + (b - a) * d + m
    print(ans)