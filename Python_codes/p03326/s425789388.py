n,m=map(int,input().split())
x=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(8):
    a=[0]*n
    for j in range(n):
        for k in range(3):
            if i>>k&1:
                a[j]+=x[j][k]
            else:
                a[j]-=x[j][k]
    ans=max(ans,abs(sum(sorted(a,reverse=1)[:m])))
print(ans)