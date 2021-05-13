def tenka17_c():
    N = int(input())
    ans = None
    for x in range(1, 3501):
        for y in range(1, 3501):
            a = N * x * y
            b = 4*x*y - N*y - N*x
            if b < 1: continue
            if a % b == 0:
                ans = (x, y, a//b)
                break
        if ans: break
    print(*ans, sep=' ')

tenka17_c()