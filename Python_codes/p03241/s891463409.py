n,m=map(int,input().split())

ans=0
for i in range(1,int(m**0.5)+1):
    if m%i==0:
        if i<=m//n:
            tmp=i
        if i>=n:
            tmp=m//i
        if tmp>ans:
            ans=tmp
print(ans)