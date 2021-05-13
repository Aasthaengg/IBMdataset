from itertools import*
from math import*
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = float("inf")
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)

N = int(input())
#N = k(k-1)//2を満たすkが存在するかをまず判定
k = ceil(sqrt(2*N))
if k*(k-1) != 2*N:
    print("No")
    exit()
print("Yes")
print(k)
#crossing pairを構成する(1からNまで各２個ずつ別々に含まれるように配置)
S = [[]for _ in range(k+1)]
num = 1
for i in range(1,k):
    for j in range(i+1,k+1):
        S[i].append(num)
        S[j].append(num)
        num +=1
for i in range(1,k+1):
    print(k-1," ".join(map(str,S[i])))