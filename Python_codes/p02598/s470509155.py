from bisect import *
from heapq import *
import math
mod = 10**9+7
N, K = map(int, input().split())
A = list(map(int, input().split()))
l = 0
r = 10**9+1
while l+1 < r:
    x = (l+r)//2
    k = 0
    for a in A:
        k += math.ceil(a/x)-1
        if k > K:
            break
    if K < k:
        l = x
    else:
        r = x
print(r)