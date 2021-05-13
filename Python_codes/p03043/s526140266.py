from decimal import Decimal
n,k=map(int,input().split())
ans=0
ans+=Decimal(max(0,(n+1-k))/n)
for i in range(1,min(k,n+1)):
    tmp=i
    tt=Decimal(1/n)
    while 0<tmp<k:
        tmp*=2
        tt=Decimal(tt/2)
        if tmp>=k:
            ans+=Decimal(tt)
print(Decimal(ans))