a, b, c = map(int, input().split())
if a == b == c and a % 2 == 0:
    print(-1)
else:
    cnt = 0
    while True:
        if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
            break
        _a = (b+c)//2
        _b = (c+a)//2
        _c = (a+b)//2
        a = _a
        b = _b
        c = _c
        cnt += 1
    print(cnt)