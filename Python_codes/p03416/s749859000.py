a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
    tmp=str(i)
    n=len(tmp)
    c=0
    for j in range((n+1)//2):
        if tmp[j]==tmp[-j-1]:
            c+=1
    if c==(n+1)//2:
        ans+=1
print(ans)