n=int(input())
a=[]
for i in range(2):
    a.append(list(map(int,input().split())))

ans=0
for k in range(n):
    s=0
    for i in range(0,k+1):
        s+=a[0][i]
    for j in range(k,n):
        s+=a[1][j]
    ans=max(ans,s)
print(ans)

