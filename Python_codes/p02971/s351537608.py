def solve():
    from bisect import bisect_left
    import sys
    n, *s = map(int, sys.stdin.read().split())
    t = sorted(s)
    for ss in s:
        x = bisect_left(t, ss)
        if x == n - 1:
            print(t[-2])
        else:
            print(t[-1])



solve()