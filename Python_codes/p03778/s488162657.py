W,a,b=list(map(int,input().split()))
ans=0
if a<b:
    ans=max(0, b-(a+W))
if a>=b:
    ans=max(0, a-(b+W))
print(ans)