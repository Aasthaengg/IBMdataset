while 1:
    try:
        a = list(map(int, input().split()))
        b=list(a)
        a.sort()
        while a[1]%a[0] != 0:
            a[1] %= a[0]
            a.sort()
        print(a[0], int(b[0]*b[1]/a[0]))
    except:
        break
