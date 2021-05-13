from math import ceil
def check(x,hp):
    hp=[hh-(b*x) for hh in hp]
    cnt=0
    for p in hp:
        if p<=0:continue
        cnt+=ceil(p/(a-b))
    return cnt<=x

n,a,b=map(int,input().split())
h=[int(input()) for i in range(n)]
lo=0
hi=10**9
while hi-lo>1:
    mid=(hi+lo)//2
    if check(mid,h):
        hi=mid
    else:
        lo=mid
ans=hi
# htとloどちらを出力すればよい？
# print(lo)
print(hi)