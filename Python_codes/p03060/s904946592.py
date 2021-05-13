n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
ans=-10*18
for i in range(1<<n):
    mask=[(i>>j)&1 for j in range(n)]
    X=0
    Y=0
    for k, m in enumerate(mask):
        if m==1:
            X+=v[k]
            Y+=c[k]
    ans=max(ans, X-Y)
    
print(ans)