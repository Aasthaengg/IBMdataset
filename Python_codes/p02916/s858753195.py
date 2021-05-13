n=int(input())
a=[int(x) for x in input().rstrip().split()]
b=[int(x) for x in input().rstrip().split()]
c=[int(x) for x in input().rstrip().split()]

ans=0
mae=float('inf')
for i in range(n):
    if mae+1==a[i]:
        ans+=c[mae-1]
    ans+=b[a[i]-1]
    mae=a[i]

print(ans)
