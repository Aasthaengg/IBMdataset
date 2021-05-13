# python3.4.2用
import math
import fractions
import bisect
import collections
import itertools
import heapq
import string
import sys
import copy
from decimal import *
from collections import deque
sys.setrecursionlimit(10**7)
MOD = 10**9+7
INF = float('inf') #無限大
def gcd(a,b):return fractions.gcd(a,b) #最大公約数
def lcm(a,b):return (a*b) // fractions.gcd(a,b) #最小公倍数
def iin(): return int(sys.stdin.readline()) #整数読み込み
def ifn(): return float(sys.stdin.readline()) #浮動小数点読み込み
def isn(): return sys.stdin.readline().split() #文字列読み込み
def imn(): return map(int, sys.stdin.readline().split()) #整数map取得
def imnn(): return map(lambda x:int(x)-1, sys.stdin.readline().split()) #整数-1map取得
def fmn(): return map(float, sys.stdin.readline().split()) #浮動小数点map取得
def iln(): return list(map(int, sys.stdin.readline().split())) #整数リスト取得
def iln_s(): return sorted(iln()) # 昇順の整数リスト取得
def iln_r(): return sorted(iln(), reverse=True) # 降順の整数リスト取得
def fln(): return list(map(float, sys.stdin.readline().split())) # 浮動小数点リスト取得
def join(l, s=''): return s.join(l) #リストを文字列に変換
def perm(l, n): return itertools.permutations(l, n) # 順列取得
def perm_count(n, r): return math.factorial(n) // math.factorial(n-r) # 順列の総数
def comb(l, n): return itertools.combinations(l, n) # 組み合わせ取得
def comb_count(n, r): return math.factorial(n) // (math.factorial(n-r) * math.factorial(r)) #組み合わせの総数
def two_distance(a, b, c, d): return ((c-a)**2 + (d-b)**2)**.5 # 2点間の距離
def m_add(a,b): return (a+b) % MOD
def lprint(l): print(*l, sep='\n')
def sieves_of_e(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]: continue
        for j in range(i * 2, n+1, i): is_prime[j] = False
    return is_prime

H,W = imn()

s = [input() for _ in range(H)]
d = [[INF for _ in range(W)] for _ in range(H)]
d[0][0] = 0
if s[0][0] == '#': d[0][0] = 1

xd = [1, 0]
yd = [0, 1]
que = deque([(0, 0)])
cnt = 0
while len(que) > 0:
    cnt += 1
    point = que.popleft()
    x = point[0]
    y = point[1]
    if x == W-1 and y == H-1: continue
    for i in range(2):
        nx = x + xd[i]
        ny = y + yd[i]
        if nx >= W or ny >= H: continue
        if s[ny][nx] == '#' and s[y][x] == '.': 
            if d[ny][nx] > d[y][x]+1:
                d[ny][nx] = d[y][x]+1
                que.append((nx,ny))
        else:
            if d[ny][nx] > d[y][x]:
                d[ny][nx] = d[y][x]
                que.append((nx,ny))
print(d[H-1][W-1])



