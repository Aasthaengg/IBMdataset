import sys
from fractions import gcd
n,k = map(int,input().split())
A = list(map(int,input().split()))
if k in A:
    print("POSSIBLE")
    sys.exit()
A.sort()
if A[n-1] < k:
    print("IMPOSSIBLE")
    sys.exit()
mod = A[0]
for i in range(1,n):
    mod = gcd(mod,A[i])
    if mod == 1 or (k%mod==0):
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")