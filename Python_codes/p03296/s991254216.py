n=int(input())
a=list(map(int,input().split()))
ans=0
l=1
v=a[0]
for i in range(1,n):
    if a[i]==v:
        l+=1
    else:
        ans+=l//2
        l=1
        v=a[i]
ans+=l//2
print(ans)