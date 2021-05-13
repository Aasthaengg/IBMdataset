n,m=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(m)]
p=list(map(int,input().split()))
ans=0
for i in range(2**n):
    ss=[0]*n
    cc=0
    for j in range(n):
        if i>>j&1:
            ss[j]=1
    for j in range(m):
        c=0
        k=s[j][0]
        for l in range(1,k+1):
            c+=ss[s[j][l]-1]
        if c%2==p[j]:
            cc+=1
    if cc==m:
        ans+=1
print(ans)

            

