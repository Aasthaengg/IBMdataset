n,m=map(int,input().split())
temp=m//n
i,ans=1,1
while i*i<=m:
    if m%i==0:
        if ans<i<=temp: ans=i
        if ans<m//i<=temp: ans=m//i
    i+=1
print(ans)