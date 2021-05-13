import bisect,collections,copy,heapq,itertools,math,string
from collections import defaultdict as D
from functools import reduce
import numpy as np
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353    

N = I()
H = LI()

# 短調非減少 H[i] <= H[i+1]
# 隣接要素を比較して大きかったら、必ず-1しておく
H[0]-=1
for i in range(N-1):
  if H[i] < H[i+1]:
    H[i+1] -= 1
  elif H[i] > H[i+1]:
    print("No")
    exit()
print("Yes")



# if N ==1:
#     print('Yes')
#     exit()
# ans = True
# for i in range(N-1):
#     if H[i] <= H[i+1]:
#         # print(i,'1')
#         continue
#     elif (not i==0) and H[i]-1 == H[i+1]:
#         if not H[i-1] == H[i]:
#             H[i] -= 1
#             # print(i,'2')
#             continue
#     # print(i,'3')
#     ans = False
#     break

# if ans:
#     print('Yes')
# else:
#     print('No')