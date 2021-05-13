k,s=map(int,input().split())
ans=0
for i in range(k+1):
    x=min(s-i,k)-max(0,s-k-i)
    if x>=0:
        ans+=x+1
print(ans)