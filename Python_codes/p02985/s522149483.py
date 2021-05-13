from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

# class Combination:
#     """
#     comb = Combination(1000000)
#     print(comb(5, 3))  # 10
#     """
#     def __init__(self, n_max, mod=10**9+7):
#         self.mod = mod
#         self.modinv = self.make_modinv_list(n_max)
#         self.fac, self.facinv = self.make_factorial_list(n_max)

#     def __call__(self, n, r):
#         return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

#     def make_factorial_list(self, n):
#         # 階乗のリストと階乗のmod逆元のリストを返す O(n)
#         # self.make_modinv_list()が先に実行されている必要がある
#         fac = [1]
#         facinv = [1]
#         for i in range(1, n+1):
#             fac.append(fac[i-1] * i % self.mod)
#             facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
#         return fac, facinv

#     def make_modinv_list(self, n):
#         # 0からnまでのmod逆元のリストを返す O(n)
#         modinv = [0] * (n+1)
#         modinv[1] = 1
#         for i in range(2, n+1):
#             modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
#         return modinv


n,k = inpl()
g = [[] for i in range(n)]
seen = [-1]*n
for i in range(n-1):
    a,b = inpl()
    g[a-1].append(b-1)
    g[b-1].append(a-1)
def p(n,i):
    count = 1
    for _ in range(i):
        count = count * n % mod
        n -= 1
    return count
def dfs(cur,par=-1):
    res = 1
    c = 0 if par == -1 else 1
    cnt = 0
    for v in g[cur]:
        if v == par:
            continue
        cnt += 1
        res *= dfs(v,cur)
        res %= mod
    return res*p(k-c-1,cnt)
print(dfs(0,-1)*k%mod)