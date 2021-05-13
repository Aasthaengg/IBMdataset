n,m,c=map(int,input().split())
b=list(map(int,input().split()))
count=0
for i in range(n):
    ans=0
    a=list(map(int,input().split()))
    for i in range(m):
        ans+=a[i]*b[i]
    if ans+c>0:
        count+=1
print(count)