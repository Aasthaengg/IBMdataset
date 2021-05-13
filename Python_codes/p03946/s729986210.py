n,t=map(int,input().split())
a=list(map(int,input().split()))
b=[0 for i in range(n)]
mi=a[0]
sa=0
for i in range(n):
    if a[i]<mi:
        mi=a[i]
    if a[i]-mi>=sa:
        sa=a[i]-mi
        b.append(sa)
ans=b.count(sa)
print(ans)