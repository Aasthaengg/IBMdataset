a, b, c = map(int, input().split())
res = 0
if a == b and a == c and a % 2 == 0:
    print(-1)
else:
    while 10 > 0:
        if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
            break
        a1 = a//2
        b1 = b//2
        c1 = c//2
        a = b1+c1
        b = a1+c1
        c = a1+b1
        res += 1
    print(res)
