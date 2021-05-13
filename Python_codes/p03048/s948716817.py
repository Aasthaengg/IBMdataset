r,g,b,n=map(int,input().split())

ans=0
for R in range(n//r+1):
    for B in range((n)//b+1):
        if (R*r+B*b-n)<=0 and (R*r+B*b-n)%g==0:
            ans+=1
            
print(ans)