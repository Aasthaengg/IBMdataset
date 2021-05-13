n=int(input())
a=[0]+[int(x) for x in input().split()]
b=[0]+[int(x) for x in input().split()]
c=[0]+[int(x) for x in input().split()]

ans=0

for i in range(n+1):
    ans+=b[a[i]]
    if i>0:
        if a[i-1]+1==a[i]:
            ans+=c[a[i-1]]
print(ans)