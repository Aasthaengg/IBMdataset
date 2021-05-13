a,b=map(int,input().split())
a=list(range(a,b+1))
ans=0
for i in range(len(a)):
    if str(a[i])==str(a[i])[::-1]:
        ans+=1
print(ans)