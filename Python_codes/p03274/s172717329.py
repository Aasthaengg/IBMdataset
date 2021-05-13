n,k=map(int,input().split())
x=list(map(int,input().split()))
xp=[xi for xi in x if xi>=0]
xm=[xi for xi in x if xi<0]
xm.sort(reverse=True)
ans=3*10**8
for i in range(k+1):
    # xpからi個のろうそくをつける。xmからはk-i個火をつける
    if i>len(xp) or k-i>len(xm):
        continue
    a=xp[i-1] if len(xp)>0 and i>0 else 0
    b=xm[k-i-1] if len(xm)>0 and k-i>0 else 0
    ans=min(ans,2*a-b,a-2*b)
print(ans)

