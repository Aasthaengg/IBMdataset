ab=[[float('inf') for j in range(401)] for i in range(401)]
n,ma,mb=map(int,input().split())
a,b,c=map(int,input().split())
ab[a][b]=c
ab[0][0]=0
for i in range(n-1):
    a,b,c=map(int,input().split())
    for j in range(400,-1,-1):
        for k in range(400,-1,-1):
            if ab[j][k]!=float('inf'):
                ab[j+a][k+b]=min(ab[j][k]+c,ab[j+a][k+b])
ans=float('inf')
a,b=ma,mb
while a<401 and b<401:
    ans=min(ans,ab[a][b])
    a+=ma
    b+=mb
if ans==float('inf'):
    ans=-1
print(ans)