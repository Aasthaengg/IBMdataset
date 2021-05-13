n=int(input())
ans=0
for i in range(1,int((n-1)**0.5)+1):
    if n%i==0:
        if i+2<=n//i:
            ans+=n//i-1
print(ans)