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
     
def digit_bin(n):
    cnt = 1
    while n > 1:
        n = n >> 1
        cnt += 1
    return cnt


def main():
    N, K = LI()
    A = LI()
    M = max(K, max(A))
    n = digit_bin(M)
    one_count = [0] * n
    pow2 = [1] * (n+1)

    for i in range(1, n+1):
        pow2[i] = pow2[i-1] * 2

    for a in A:
        i = 0
        while a:
            if a & 1 == 1:
                one_count[i] += 1
            i += 1
            a = a >> 1
    # import pdb
    # pdb.set_trace()
    cur = 0
    ans = 0
    for i in range(n)[::-1]:
        # zero is more
        b = 0
        if one_count[i] <= N - one_count[i]:
            b = 1
            if cur + pow2[i] > K:
                b = 0
        cur += pow2[i] * b
        if b == 1:
            ans += pow2[i] * (N-one_count[i])
        else:
            ans += pow2[i] * one_count[i]

    print(ans)


main()

