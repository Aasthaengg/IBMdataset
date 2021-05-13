from decimal import Decimal as d 
n,k=map(int,input().split())
ans=d(0)
for i in range(1,n+1):
    x=d(1)
    if i>=k:
        ans+=d(x)
    else:
        while i<k:
            x=d(x)/d(2)
            i*=2
        ans+=x
print(d(ans)/d(n))
        

        
