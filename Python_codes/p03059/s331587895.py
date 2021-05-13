A,B,T=list(map(int,input().split()))
ans=0
for t in range(1,T+1):
    if t%A==0:
        ans+=B
print(ans)
