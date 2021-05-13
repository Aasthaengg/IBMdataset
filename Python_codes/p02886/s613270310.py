n=int(input())
d=list(map(int,input().split()))
ans=0
for i in range(n-1,-1,-1):
    for j in range(0,n):
        if i<=j:
            break
        else:
            ans+=d[i]*d[j]
print(ans)