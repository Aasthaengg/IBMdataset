# ABC057 D - Maximum Average Sets
from collections import defaultdict
from math import factorial
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
def perm(n,r):
    return factorial(n)//factorial(n-r)
 
def comb(n,r):
    return perm(n,r)//factorial(r)

n,a,b=nm()
v=sorted(nl(), reverse=True)

if v[0]==v[a-1]:
    n = 0
    for vv in v:
        if vv!=v[0]: break
        n += 1

    ans = 0
    for k in range(a, min(b,n)+1):
        ans += comb(n, k)

else:
    n = k = 0
    for i,vv in enumerate(v):
        if vv==v[a-1]:
            if i<a: k += 1
            n += 1
    ans = comb(n,k)

print(sum(v[:a])/a)
print(ans)
