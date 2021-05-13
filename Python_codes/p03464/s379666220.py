k=int(input())
a=[int(i) for i in input().split()]
l=2
r=3
for i in range(k-1,-1,-1):
    l=(l+a[i]-1)//a[i]*a[i]
    r=(r+a[i]-1)//a[i]*a[i]
if l==r:
    print(-1)
else:
    print(l,r-1)
