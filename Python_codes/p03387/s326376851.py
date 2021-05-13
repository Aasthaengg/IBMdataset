a,b,c=map(int,input().split())
num1=max(a,b,c)
if num1==a:
    num2=a-b
    num3=a-c
elif num1==b:
    num2=b-a
    num3=b-c
else:
    num2=c-a
    num3=c-b
num4=abs(num2-num3)
if num4%2==0:
    print((num2+num3)//2)
else:
    print((num2+num3)//2+2)
