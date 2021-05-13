def sumitb2019_f():
    t1, t2 = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())

    p = (a1 - b1) * t1
    q = (a2 - b2) * t2
    if p > 0:
        p *= -1
        q *= -1

    if p + q < 0:
        ans = 0
    elif p + q == 0:
        ans = 'infinity'
    else:
        s, t = divmod(-p, p + q)
        if t == 0: ans = s * 2
        else: ans = s * 2 + 1
    print(ans)

if __name__ == '__main__':
    sumitb2019_f()