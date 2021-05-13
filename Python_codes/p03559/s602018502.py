def resolve():
    import bisect
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        btest = b[i]
        aind = bisect.bisect_left(a,btest)
        cind = bisect.bisect_right(c, btest)
        ans += aind * (len(c)-cind)
    print(ans)
resolve()