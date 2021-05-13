import math
from functools import reduce
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
def hcf(l):
    return reduce(math.gcd, l)
gcd = hcf(A)
m = max(A)
if k%gcd == 0 and k<=m:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
