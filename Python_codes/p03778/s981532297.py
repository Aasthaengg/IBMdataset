w,a,b=map(int,input().split())
ans=max(a,b)-min(a,b)-w
if ans<=0:
    print(0)
else:
    print(ans)
