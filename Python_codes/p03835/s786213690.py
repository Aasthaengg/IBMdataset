k,s=map(int,input().split())
ans=0
for i in range(k+1):
    if s-i>=0:
        for j in range(min(s-i+1,k+1)):
            if s-i-j<=k and s-i-j>=0:
                ans+=1
print(ans)
