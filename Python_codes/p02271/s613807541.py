from functools import lru_cache

@lru_cache(maxsize = None)
def canProd(i,m):
     
    if m == 0:
        return True
    if i >= n:
        return False
 
    res = canProd(i+1,m) or canProd(i+1,m-a[i])
    return res
 
 
n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
m = [int(x) for x in input().split()]

rs = [None]*2001

maxm = max(m)
minm = min(m)

for i in range(minm,maxm+1):
    if canProd(0,i):
        rs[i] = "yes"
    else:
        rs[i] = "no"

for i in m:
    print(rs[i])