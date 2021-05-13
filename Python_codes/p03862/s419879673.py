def solve():
    n, x = map(int, input().split())
    s = list(map(int, input().split()))
    cnt, tmp, prv = 0, 0, 0

    if s[0] > x:
        cnt += s[0] - x
        s[0] = x

    for y in s:
        if prv + y > x:
            tmp = prv + y - x
            cnt += tmp
            prv = y - tmp
        else:
            prv = y
    print(cnt)


solve()
