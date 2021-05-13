a,b,c=map(int,input().split())
num1=0
num2=0
num3=0
if a==b and b==c and a%2==0:
    print(-1)
else:
    for i in range(a*b*c):
        if a%2==1 or b%2==1 or c%2==1:
            break
        num1=a//2
        num2=b//2
        num3=c//2
        a=num2+num3
        b=num3+num1
        c=num1+num2
    print(i)
