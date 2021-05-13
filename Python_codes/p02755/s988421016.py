def check(x):
    if (x*10)//100>=b and (x*8)//100>=a: return True
    else: return False

a,b=map(int,input().split())
l=0 
r=10**9
while(l<r):
    mid=(l+r)//2
    if check(mid):r=mid
    else: l=mid+1
print(l if (l*10)//100==b and (l*8)//100==a else -1)
