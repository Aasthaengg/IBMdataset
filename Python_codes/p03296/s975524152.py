n=int(input())
l=list(map(int,input().split()))
c=l[0]
ans=0
for i in range(1,n):
    if l[i]==c:
        ans+=1
        c=10001
    else:c=l[i]
print(ans)