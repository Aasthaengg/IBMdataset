from collections import deque,defaultdict,Counter
from itertools import accumulate
import bisect
from heapq import heappop,heappush
from fractions import gcd
from copy import deepcopy
import math
Mod = 1000000007



def main(): #startline-------------------------------------------
    S = input()
    N = len(S)
    p = [0,0,0,1]
    for i in range(N):
        if S[i] == "A":
            p[0] += p[3]
            p[0] %= Mod
        elif S[i] == "B":
            p[1] += p[0]
            p[1] %= Mod
        elif S[i] == "C":
            p[2] += p[1]
            p[2] %= Mod
        elif S[i] == "?":
            p[2] = p[2]*3 + p[1]
            p[1] = p[1]*3 + p[0]
            p[0] = p[0]*3 + p[3]
            p[3] *= 3
            for l in range(4):
                p[l] %= Mod

    print(p[2])
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