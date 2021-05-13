n,m,c=map(int,input().split())
b=list(map(int,input().split()))
a=[0]*n
for i in range(n):
    a[i]=list(map(int,input().split()))

ans=0

for i in range(n):
    p=0
    for k in range(m):
        p+=a[i][k]*b[k]
    p+=c
    if p>0:
        ans+=1

print(ans)