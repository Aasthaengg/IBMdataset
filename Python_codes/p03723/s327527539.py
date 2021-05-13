a,b,c=map(int,input().split())

if a==b==c and a%2==0:
    print(-1)
else:
    num=0
    while True:
        if a%2==1 or b%2==1 or c%2==1:
            break
        num+=1
        l0=(b+c)/2
        l1=(c+a)/2
        l2=(a+b)/2
        a,b,c=l0,l1,l2
    print(num)