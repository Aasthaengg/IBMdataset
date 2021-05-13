try:
    while True:
        x=list(sorted(map(int, input().split())))
        a=x[0]
        b=x[1]
        while b%a != 0:
            c=a
            a=b%a
            b=c
        print(a, x[0]*x[1]//a)
except EOFError:
    pass