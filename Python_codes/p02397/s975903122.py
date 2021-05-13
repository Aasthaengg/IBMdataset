while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    if a>b:
        num=a
        a=b
        b=num
    print(a,b)