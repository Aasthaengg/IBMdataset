import collections
import math

def C(n, r):
    if n == 0 or r == 0: return 1
    return C(n, r-1) * (n-r+1) // r 

a = list(input())
n = len(a)
aa = collections.Counter(a)
ans = C(n,2)
for i in aa:
    if aa[i] >= 2:
        ans += -C(aa[i],2)
print(ans+1)