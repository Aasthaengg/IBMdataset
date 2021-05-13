import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
def debug(*args):
    if debugmode:
        print(*args)
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def INT(): return int(input())
def FLOAT(): return float(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7
dx = [0, 1, 0, -1, 1, -1, -1, 1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
debugmode = True

#素因数分解
def prime_factorize(n):
    a = []
    a.append(1)
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    
    b = [[],[]]
    cnt = 1
    for i in range(len(a)+1):
        if i > 0 and i < len(a):
            if a[i] == a[i-1]:
                cnt += 1
            else:
                b[0].append(a[i-1])
                b[1].append(cnt)
                cnt = 1
        if i == len(a) and i > 0:
            b[0].append(a[i-1])
            b[1].append(cnt)
        elif i == len(a) and i == 0:
            b[0].append(a[i])
            b[1].append(cnt)
    return b

#コンビネーション(特殊例)
def cmb(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

N = 10**5 + 100
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

n, m = MAP()
mar = prime_factorize(m)
arr = mar[1]
ans = 1
for i in range(1, len(arr)):
    ans *= cmb(arr[i] + n - 1, arr[i])
    ans %= mod
print(ans)
