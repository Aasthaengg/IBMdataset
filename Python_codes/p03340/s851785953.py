from collections import deque,defaultdict,Counter
from itertools import accumulate
import bisect
from heapq import heappop,heappush
from fractions import gcd
from copy import deepcopy
import math
import queue
#import numpy as np
Mod = 1000000007




def main(): #startline--------------------------------------------
    N = int(input())
    A = list(map(int,input().split()))
    r = 0
    pinf = 0
    ans = 0
    for l in range(N):
        while (r < N) and ((pinf ^ A[r]) == (pinf + A[r])):
            pinf += A[r]
            r += 1
        ans += r-l
        if l == r:
            r += 1
        else:
            pinf -= A[l]

    print(ans)
if __name__ == "__main__":
    main() #endline===============================================





def sieve_of_eratosthenes(n):
    if not isinstance(n,int):
        raise TypeError("n is not int")
    if n<2:
        raise ValueError("n < 2 is not effective")
    prime = [1]*(n+1)
    for i in range(2,int(math.sqrt(n))):
        if prime[i] == 1:
            for j in range(2*i,n):
                if j%i == 0:
                    prime[j] = 0
    res = []
    for i in range(2,n):
        if prime[i] == 1:
            res.append(i)
    return res

class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
    
    def findroot(self,x):
        if x == self.parent[x]:
            return x
        else:
            y = self.parent[x]
            y = self.findroot(self.parent[x])
            return y
    
    def union(self,x,y):
        px = self.findroot(x)
        py = self.findroot(y)
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py

    def same_group_or_no(self,x,y):
        return self.findroot(x) == self.findroot(y)