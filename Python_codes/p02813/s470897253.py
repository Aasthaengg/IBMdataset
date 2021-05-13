import itertools   # accumulate, compress, permutations(nPr), combinations(nCr)
# import bisect      # bisect_left(insert位置), bisect_right(slice用)
import math        # factorical（階乗) # hypot(距離)
# import heapq
# from fractions import gcd # Python3.5以前 # lcm（最小公倍数） = (a*b)//gcd(a,b)
# from fractions import Fraction
# from math import gcd # Python3.6以降
# --------------------------------------------------------------

n = int(input())
p = list(input().split())
q = list(input().split())
nlis = sorted(p)

cntp = 0
cntq = 0

for idx, i in enumerate(itertools.permutations(nlis,n)):
    if list(i)==p:
        cntp = idx
    if list(i)==q:
        cntq = idx

print(abs(cntp-cntq))