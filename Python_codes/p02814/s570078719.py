from collections import defaultdict, deque
import sys, heapq, bisect, math, itertools, string, queue, copy, time
from fractions import gcd
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7
EPS = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)

def lcm(a, b):
    return a*b//gcd(a,b)
n, m = map(int, input().split())
a_array = np.array(list(map(int, input().split())))
c_array = np.copy(a_array)
while True:
    c_array //= 2
    if 1 in c_array%2:
        is_valid = not (0 in c_array%2)
        break
b_array = a_array//2
if is_valid:
    k = b_array[0]
    for i in range(n):
        k = lcm(k, b_array[i])
    ans = (m//k + 1)//2 
    print(ans)    
else:
    ans = 0
    print(ans)