n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    if a[a[i]-1]==i+1 and a[i]==a[a[a[i]-1]-1]:
        ans+=1
        a[a[i]-1]=0
        a[i]=0
print(ans)
