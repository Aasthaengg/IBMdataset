a,b,c=map(int,input().split())

if b>=a:
    print(c)
else:
    if c-a+b<=0:
        print('0')
    else:
        print(c-a+b)