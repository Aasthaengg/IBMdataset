import sys, re
from collections import deque, defaultdict, Counter
from math import exp, ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd, e
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
import random
import time
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

start = time.time()

D = INT()
C = LIST()
s = [LIST() for _ in range(D)]

def compute_score(out):
    score = 0
    last = [0]*26

    for d in range(D):
        last[out[d]] = d+1
        for i in range(26):
            score -= (d+1-last[i])*c[i]
        score += s[d][out[d]]

    return score

def decrease(d, j):  # d:日にち, j:開催するコンテスト
    tmp = 0
    for i in range(26):
        if i == j: continue
        tmp += C[i]*(d-last[i])
    return tmp 

def init():  # 貪欲でとった解を1度保存する
    global now
    for i in range(D):  # i+1日目
        ma = -INF
        ma_idx = None
        for j in range(26):  # 開催するコンテスト
            tmp = now
            tmp += s[i][j]
            tmp -= decrease(i+1, j)
            if tmp > ma:
                ma = tmp
                ma_idx = j
        now = ma
        last[ma_idx] = i+1
        score[ma_idx] += s[i][ma_idx]
        for j in range(26):
            score[j] -= C[j]*(i+1-last[j])
        last[ma_idx] = i+1
        ans[i] = ma_idx+1

def update(d, q):  # d日目のところをqに変更する
    d -= 1
    q -= 1
    c = ans[d]-1  # c:更新前
    ans[d] = q+1
    last_c = 0
    last_q = 0
    score_c = 0
    score_q = 0
    for j in range(D):
        if ans[j]-1 == c:
            last_c = j+1
            score_c += s[j][c]
        elif ans[j]-1 == q:
            last_q = j+1
            score_q += s[j][q]
        score_c -= C[c] * (j+1 - last_c)
        score_q -= C[q] * (j+1 - last_q)
    score[c] = score_c
    score[q] = score_q

def swap(d):  # d日目とd+1日目の開催を入れ替える
    update(d, ans[d])
    update(d+1, ans[d-1])

ans = [0]*D
last = [0]*26
score = [0]*26
now = 0

init()

TL = 1.8 - (time.time()-start)
start = time.time()
T0 = 2e3
T1 = 6e2
T = T0
randint = random.randint
rand = random.random
while 1:
    t = (time.time()-start)/TL
    if t >= 1:
        break
    T = pow(T0, 1-t)*pow(T1, t)
    if rand() < 0.5:  # 1点変更
        d = randint(1, D)
        q = randint(1, 26)
        old = ans[d-1]
        old_score = score.copy()
        s_old = sum(score)
        update(d, q)
        s_new = sum(score)
        if s_new <= s_old and exp((s_new-s_old)/T) <= rand():  # 戻す確率
            score = old_score
            ans[d-1] = old
    else:  # 2点入れ替え
        d = randint(1, D-1)
        old = ans[d-1]
        old_score = score.copy()
        s_old = sum(score)
        swap(d)
        s_new = sum(score)
        if s_new <= s_old and exp((s_new-s_old)/T) <= rand():
            score = old_score
            ans[d-1] = old

print(*ans, sep="\n")
