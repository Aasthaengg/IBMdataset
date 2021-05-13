#editorial https://ami-atcoder.hatenablog.com/entry/20191018/1571386871
n=int(input())
pre=int(input())
if pre!=0:print(-1);exit()
ans=0
for i in range(n-1):
    x=int(input())
    if x==pre+1:ans+=1
    elif pre<x:print(-1);exit()
    else:ans+=x
    pre=x
print(ans)