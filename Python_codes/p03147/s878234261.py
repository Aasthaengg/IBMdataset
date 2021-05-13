n=int(input())
l=list(map(int,input().split()))
ans=0
f=1
m=max(l)
for j in range(m):
    for i in range(n):
        if l[i]==0:
            f=1
        elif f==0:
            l[i]-=1
        else:
            ans+=1
            l[i]-=1
            f=0
    f=1
print(ans)