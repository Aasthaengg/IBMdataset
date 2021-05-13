while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print("{a} {b}".format(a=min(a,b), b=max(a,b)))