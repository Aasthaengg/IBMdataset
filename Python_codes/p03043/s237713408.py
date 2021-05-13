import decimal
n,k=map(int,input().split())
num1=1
num2=0
for i in range(20):
    if num1>=k:
        break
    num1*=2
    num2+=1
num=n*(2**num2)
num1=num2
num3=0
for i in range(1,n+1):
    if i*(2**(num2-1))>=k:
        num2-=1
    if i>=k:
        num3+=2**num1
    else:
        num3+=2**(num1-num2)
print(decimal.Decimal(num3/num))
