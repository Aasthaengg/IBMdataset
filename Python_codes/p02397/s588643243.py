while True:
    a,b = map(int,input().split())
    if a ==0 and b ==0:
        break
    else:
        if a<=b:
            print(a,b)
        else:
            a,b =b,a
            print(a,b)