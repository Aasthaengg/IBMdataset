def slove():
    import sys
    import bisect
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    a = list(map(int, input().rstrip('\n').split()))
    b = list(map(int, input().rstrip('\n').split()))
    c = list(map(int, input().rstrip('\n').split()))
    a.sort()
    b.sort()
    c.sort()
    t = 0
    for v in b:
        an = bisect.bisect_left(a, v)
        cn = n - bisect.bisect_right(c, v)
        t += (an * cn)
    print(t)


if __name__ == '__main__':
    slove()
