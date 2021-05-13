N = int(input())
A = list(map(int, input().split()))
from fractions import gcd
from math import ceil
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
ans = 0
d = Counter(A)
if N%2==1:
    for i in range(0,N,2):
        # print(i)
        if i==0:
            if d[i]!=1:
                # print('A',A)
                break
        elif d[i]!=2:
            # print('B',i)
            break
    else:
        ans = pow(2,(N-1)//2,10**9+7)
else:
    for i in range(1,N,2):
        if d[i]!=2:
            # print(i)
            break
    else:
        ans = pow(2,N//2,10**9+7)
print(ans)