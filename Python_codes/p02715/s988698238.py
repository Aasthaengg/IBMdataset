import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def pow(x, n):
  ans = 1
  while(n > 0):
    if(bin(n & 1) == bin(1)):
      ans = ans*x
      ans %= mod
    x = x*x
    x %= mod
    n = n >> 1
  return ans % mod

nums = [0 for _ in range(10**5 + 1)]

def f(i, N, K):
    # i no baisuu
    # i = K, K-1, ..., 1
    cnt = pow(K // i, N)
    # subtract 2i, 3i, 4i, ...
    j = i
    while j + i <= K:
        cnt -= nums[j+i]
        j += i
    nums[i] = cnt
    return nums[i]

def main():
    N, K = LI()
    cnt = 0
    for i in range(1, K+1)[::-1]:
        cnt += (i * f(i, N, K) % mod)
        cnt %= mod
    print(cnt)

main()

