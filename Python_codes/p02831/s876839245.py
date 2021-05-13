import bisect,collections,copy,heapq,itertools,math,string
# from fractions import gcd
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

# N = I()
A,B = LI()
#AB = [LI() for _ in range(N)]
#A,B = zip(*AB)
#Ap = np.array(A)
#C = np.zeros(N + 1)

# 最小公倍数 = A * B // 最大公約数
ans = A * B // math.gcd(A,B)
print(ans)

# if ans:
#     print('Yes')
# else:
#     print('No')