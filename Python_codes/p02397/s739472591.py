while True:
    a,b=map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        t=a
        a=b
        b=t
    print("{0} {1}".format(a,b))