n,a,b=map(int,input().split())
X=list(map(int,input().split()))
ans=0
for i in range(n-1):
    if (X[i+1]-X[i])*a<b:
        ans+=(X[i+1]-X[i])*a
    else:
        ans+=b
print(ans)