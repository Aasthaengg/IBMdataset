n,m,c=map(int,input().split())
b=list(map(int,input().split()))
ans=0
for _ in range(n):
    a=list(map(int,input().split()))
    calc=c
    for j in range(m):
        calc+=a[j]*b[j]
    if calc>0:
        ans+=1
print(ans)
