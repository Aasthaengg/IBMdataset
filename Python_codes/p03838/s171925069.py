x,y=map(int,input().split())
ans=float("INF")
for i in range(4):
    n,m=x,y
    f=0
    if i//2:n=-x;f+=1
    if i%2:m=-y;f+=1

    ans=min(ans,float("INF") if n>m else m-n+f)
print(ans)