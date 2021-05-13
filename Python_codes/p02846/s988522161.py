t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
x = (a1 - b1) * t1
y = (a2 - b2) * t2
p, q = x // abs(x), y // abs(y)
#print(x, y)
if x + y == 0:
    print('infinity')
else:
    l, r = 0, 10 ** 40 + 1
    ans = 0
    while r - l > 1:
        m = (l + r) // 2
        t = (x + y) * m
        if (t - y < 0) ^ (t <= 0):
            l = m
        else:
            r = m
    ans += l
    l, r = 0, 10 ** 40 + 1
    while r - l > 1:
        m = (l + r) // 2
        t = (x + y) * m
        if (t + x <= 0) ^ (t < 0):
            l = m
        else:
            r = m
    ans += l
    print(ans)
