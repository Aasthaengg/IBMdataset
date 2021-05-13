S = int(input())

if S <= 10**9:
    ans = [0, 0, S, 0, 0, 1]
    print(*ans)
    exit()
else:
    if S == 10 ** 18:
        ans = [0, 0, 10 ** 9, 0, 0, 10 ** 9]
        print(*ans)
        exit()
    mod = S % (10 ** 9)
    syou = S // (10 ** 9)
    x3 = 10 ** 9 - mod
    y3 = syou + 1
    ans = [0, 0, 10 ** 9, 1, x3, y3]
    print(*ans)
