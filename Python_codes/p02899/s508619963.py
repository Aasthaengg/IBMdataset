import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
from numba import njit
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = LI()

B = range(1,N+1)
AB = zip(A,B)
# print(*AB)
sAB = sorted(AB)
# print(*sAB)
_,ans=zip(*sAB)
print(*ans)


#AB = [LI() for _ in range(N)]
#A,B = zip(*AB)
#Ap = np.array(A)
#C = np.zeros(N + 1)
# index 順 要素のindex

# ans = []
# for i in range(N):
#     ans.append(A.index(i+1)+1)
# print(*ans)