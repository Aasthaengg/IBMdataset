n=int(input())
*a, =map(int,input().split())
a=[a[i]-(i+1) for i in range(n)]
a=sorted(a)

c1=a[n//2-1]
c2=a[n//2]
ans=float('inf')

for c in [c1,c2]:
    tmp=0
    for i in range(n):
        tmp+=abs(a[i]-c)
    ans=min(ans, tmp)
print(ans)