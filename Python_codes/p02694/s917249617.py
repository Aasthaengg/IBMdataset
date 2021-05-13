from decimal import Decimal
x=int(input())
n=Decimal("100")
ans=0
while True:
    ans+=1
    n*=Decimal("1.01")
    n//=1
    if n>=x:
        print(ans)
        break