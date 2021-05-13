N,x=map(int,input().split())
a=list(map(int,input().split()))
eat=0
for i in range(N-1):
    num1=a[i]
    num2=a[i+1]
    if num1+num2>x:
        buf=min(num1+num2-x,num2)
        eat=eat+buf
        num2=num2-buf
        if num1>x:
            buf=num1-x
            eat=eat+buf
            num1=num1-buf
    a[i]=num1
    a[i+1]=num2
    #print(a)
print(eat)