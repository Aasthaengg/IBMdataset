d,n =map(int,input().split())
if d==0:
    if n==100:
        print(101)
    else:
        print(n)
else:
    if n==100 and d==1:
        print(100**1*100+100)
    elif n==100 and d==2:
        print(100**2*100+10000)
    else :
        print(100**d*n)