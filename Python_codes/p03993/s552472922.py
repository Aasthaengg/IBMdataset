n=int(input())
a=list(map(int,input().split()))
flag=[0]*n
ans=0
for i in range(n):
    if flag[i]==0:
        if (a[a[i]-1]-1)==i:
            ans+=1
            flag[i]=1
            flag[a[i]-1]=1
print(ans)