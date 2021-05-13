A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=min(a)+min(b)
for i in range(M):
    x,y,c=map(int,input().split())
    x-=1; y-=1
    point=a[x]+b[y]-c
    ans=min(point,ans)
print(ans)