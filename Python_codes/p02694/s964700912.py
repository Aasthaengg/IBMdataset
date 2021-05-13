from decimal import Decimal
k=int(input())
num=100
ans=0
while k>num:
    num=int(Decimal(num)*Decimal(101)/Decimal(100))
    ans+=1
print(ans)