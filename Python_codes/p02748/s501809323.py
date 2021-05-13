a,b,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
xyc=[list(map(int,input().split())) for _ in range(m)]
a1=sorted(a)
b1=sorted(b)
price=a1[0]+b1[0]
ans=float('inf')
for i in range(m):
    x=a[xyc[i][0]-1]+b[xyc[i][1]-1]-xyc[i][2]
    if x<ans:
        ans=x
print(min(price,ans))