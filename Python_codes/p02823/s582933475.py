n,a,b=map(int,input().split())

if (a-b)%2==0:
    print(abs(a-b)//2)
else:
    a,b=min(a,b),max(a,b)
    can1=(a)+((b-a)-1)//2
    a,b=n-b+1,n-a+1
    can2=(a)+((b-a)-1)//2
    print(min(can1,can2))