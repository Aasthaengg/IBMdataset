from math import ceil 
n,a,b=map(int,input().split())
l=[int(input()) for i in range(n)]
def check(x):
    c=0
    l1=[i-b*x for i in l]
    for i in l1: 
         if i<=0:
             continue 
         c+=ceil((i)/(a-b))
    return c<=x
lo=0 
ans=-1 
hi=10**9+4 
while lo<=hi:
    mi=(lo+hi)>>1 
    if check(mi):
        ans=mi 
        hi=mi-1
    else:
        lo=mi+1 
print(ans)
