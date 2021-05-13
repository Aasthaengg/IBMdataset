n,m=map(int,input().split())
ans=0
mm=m//2
if n>=mm:
    ans=mm
else:
    w=(mm-n)//2
    ans=n+w
print(ans)