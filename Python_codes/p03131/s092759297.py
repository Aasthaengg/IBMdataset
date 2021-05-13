k, a, b =  map(int, input().split())
if a >= b or k < a:
    print(1 + k)
else:
    s = k - a + 1
    t = s // 2
    if s % 2 == 0:
        if (a + (b - a) * t) > 1 + k:
            print(a + (b - a) * t)
        else:
            print(1 + k)
    else:
        if (a +(b - a) * t + 1) > 1 + k:
            print(a +(b - a) * t + 1)
        else:
            print(1 + k)