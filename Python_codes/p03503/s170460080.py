n=int(input())
f=[[] for i in range(n)]
for i in range(n):
    f[i]=list(map(int,input().split()))
p=[[] for i in range(n)]
for i in range(n):
    p[i]=list(map(int,input().split()))
ans=-10000000000
for i in range(1,1024):
    x=[]
    pro=0
    for j in range(10):
        x.append(i%2)
        i=i//2
    for j in range(n):
        c=0
        for k in range(10):
            if x[k]==f[j][k]==1:
                c+=1
        pro+=p[j][c]
    ans=max(ans,pro)
print(ans)
