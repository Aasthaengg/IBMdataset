n=int(input())
P=list(map(int,input().split()))
ans=0
minp=n+1
for i in range(n):
    minp=min(minp,P[i])
    if minp==P[i]:
        ans+=1
print(ans)