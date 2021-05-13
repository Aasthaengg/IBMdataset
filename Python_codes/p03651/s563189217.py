import sys
from fractions import gcd
from functools import reduce

n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k in arr:
    print("POSSIBLE")
    sys.exit()

if k > max(arr):
    print("IMPOSSIBLE")
    sys.exit()

div = reduce(gcd, arr)

print("POSSIBLE" if k % div == 0 else "IMPOSSIBLE")