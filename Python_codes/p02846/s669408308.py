def f():
    t0, t1 = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]
    sa = t0*a[0] + t1*a[1]
    sb = t0*b[0] + t1*b[1]
    if sa == sb:
        return 'infinity'
    if sa > sb:
        a, b = b,a
        sa, sb = sb, sa
    # sa < sb
    if b[0] > a[0]:
        return 0

    delta = sb - sa

    ans = 1
    d0 = (a[0]-b[0])*t0
    if d0%delta == 0:
        ans += 1
    count = (d0-1)//delta
    ans += 2 * count
    return ans


print(f())