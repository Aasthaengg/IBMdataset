n,m=map(int,input().split())
a=sorted([int(i) for i in input().split()])
import bisect

def hantei(now):
    num=0
    for ax in a:
        bi = bisect.bisect_left(a,now-ax)
        num+= bi
#         print(now,ax,bi)
    return n**2-num

mi = a[0]*2-1
ma = a[-1]*2+1
kotae=ma
while mi<ma:
    now=(mi+ma)//2
    which = hantei(now)<=m#なんか判定
    if which:
        ma=now
        kotae=now
    else:
        mi=now+1
kotae-=1

suma=[0]*(n+1)
suma[-2]=a[-1]
for i in range(n-2,-1,-1):
    suma[i] = suma[i+1]+a[i]
    
ans=0
kazu=0
for ax in a:
    bi = bisect.bisect_left(a,kotae-ax)
    ans+= (n-bi)*ax+suma[bi]
    kazu+=n-bi
print(ans-(kazu-m)*kotae)
