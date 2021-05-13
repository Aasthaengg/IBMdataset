import sys
sys.setrecursionlimit(1000000000)
import math
from math import gcd
def lcm(a, b): return a * b // gcd(a, b)
from itertools import count, permutations, chain, product
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
INF = float('inf')
N1097 = 10**9 + 7

def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok

def get_inv(n, modp):
    return pow(n, modp-2, modp)

def factorials_list(n, modp):    # 10**6
    fs = [1]
    for i in range(1, n+1):
        fs.append(fs[-1] * i % modp)
    return fs

def invs_list(n, fs, modp):     # 10**6
    invs = [get_inv(fs[-1], modp)]
    for i in range(n, 1-1, -1):
        invs.append(invs[-1] * i % modp)
    invs.reverse()
    return invs

def comb(n, k, modp):
    num = 1
    for i in range(n, n-k, -1):
        num = num * i % modp
    den = 1
    for i in range(2, k+1):
        den = den * i % modp
    return num * get_inv(den, modp) % modp

def comb_from_list(n, k, modp, fs, invs):   
    return fs[n] * invs[n-k] * invs[k] % modp

#

class UnionFindEx:
    def __init__(self, size):
        #正なら根の番号、負ならグループサイズ
        self.roots = [-1] * size
    def getRootID(self, i):
        r = self.roots[i]
        if r < 0:   #負なら根
            return i
        else:
            r = self.getRootID(r)
            self.roots[i] = r
            return r
    def getGroupSize(self, i):
        return -self.roots[self.getRootID(i)]
    def connect(self, i, j):
        r1, r2 = self.getRootID(i), self.getRootID(j)
        if r1 == r2:
            return False
        if self.getGroupSize(r1) < self.getGroupSize(r2):
            r1, r2 = r2, r1
        self.roots[r1] += self.roots[r2]    #サイズ更新
        self.roots[r2] = r1
        return True

Yes = 'Yes'
No = 'No'


def main():
    N = ii()
    X = input()
    X_POP = X.count('1')
    X_POP_P = X_POP + 1
    X_POP_N = X_POP - 1
    FX_P = 0
    FX_N = 0
    for i, b in enumerate(X):
        FX_P <<= 1
        FX_N <<= 1
        if b=='1':
            FX_P += 1
            FX_N += 1
        FX_P %= X_POP_P
        FX_N %= X_POP_N or 1
    #
    def popcount(n):
        return bin(n).count('1')
    @lru_cache(None)
    def f(n):
        if n==0:
            return 0
        else:
            return f(n % popcount(n)) + 1
    ans = []
    for i, b in enumerate(reversed(X)):
        if b=='0':
            fx = f((FX_P + pow(2, i, X_POP_P)) % X_POP_P)+1
        else:
            if X_POP_N==0:
                fx = 0
            else:
                fx = f((FX_N - pow(2, i, X_POP_N)) % X_POP_N)+1
        ans.append(fx)
    print(*reversed(ans))



main()

