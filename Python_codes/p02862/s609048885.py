x,y=map(int,input().split())
a=(2*x)-y
b=(2*y)-x
if a%3==0 and b%3==0 and a>=0 and b>=0:
    a=a//3
    b=b//3
    c=a+b
    a1=1
    a2=1
    n3=10**9+7
    for i in range(a):
        a1*=c-i
        a2*=i+1
        a1%=n3
        a2%=n3
    a2=pow(a2,n3-2,n3)
    print((a1*a2)%n3)
else:
    print(0)
