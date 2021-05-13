from decimal import Decimal
n=int(input())
ans=0
for i in range(n):
    x,y=map(str,input().split())
    if y=="BTC":
        ans+=Decimal(380000*Decimal(x))
    else:
        ans+=Decimal(x)
print(ans)