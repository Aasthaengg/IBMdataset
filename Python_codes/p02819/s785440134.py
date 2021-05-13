import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

x = inp()
serach_number = 100003
 
def sieve_of_eratosthenes(target):
    dest = int(math.sqrt(target))
    target_list = list(range(2, target + 1))
    prime_list = []
 
    while True:
        num_min = min(target_list)
        if num_min >= dest:
            prime_list.extend(target_list)
            break
        prime_list.append(num_min)
 
        i = 0
        while True:
            if i >= len(target_list):
                break
            elif target_list[i] % num_min == 0:
                target_list.pop(i)
            i += 1
    return prime_list

data = sieve_of_eratosthenes(serach_number)

for i in data:
    if i >= x:
        print(i)
        break

