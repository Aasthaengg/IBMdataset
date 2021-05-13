import sys
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(n):
    if a[i]>=b[i]:
        a[i]=a[i]-b[i]
        ans+=b[i]
    else:
        ans+=a[i]
        b[i]-=a[i]
        a[i]=0
        ans+=min(b[i],a[i+1])
        a[i+1]=max(0,a[i+1]-b[i])
        
   
print(ans)
        
        
    
    
