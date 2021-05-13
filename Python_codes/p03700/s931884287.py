# ABC063 D - Widespread
def check(x,hp):
    hp=[hh-(b*x) for hh in hp]
    explosion=0
    for hhh in hp:
        if hhh<=0:continue
        if hhh%(a-b)==0:
            explosion+=hhh//(a-b)
        else:
            explosion+=hhh//(a-b)+1
    return explosion<=x

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
print(lo+1)