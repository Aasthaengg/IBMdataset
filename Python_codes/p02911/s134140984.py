import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
from numba import njit
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

# N = I()
N,K,Q = LI()
A = [I() for _ in range(Q)]

c = collections.Counter(A)
# print(c)

B = np.zeros(N,dtype='int')
for i in range(1,N+1):
    B[i-1] = c[i]

# print(B)
ans = (B - Q + K) > 0
for b in ans:
    # print(b)
    if b:
        print('Yes')
    else:
        print('No')

#A,B = zip(*AB)
# A = np.array(_A)

# B = np.zeros(N)
# B[0:-K+1] = A

# 和 - 自分の得点
# B_sum = np.sum(B)
# C = B - B_sum
# print(C)
# print(np.where(B > -K, True, False))
# print(C>-K)

# if ans:
#     print('Yes')
# else:
#     print('No')