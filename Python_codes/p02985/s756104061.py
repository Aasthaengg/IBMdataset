import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
INF = float("inf")
MOD = 10**9+7

kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n):
    return kaijo_memo[n]
  if(len(kaijo_memo) == 0):
    kaijo_memo.append(1)
  while(len(kaijo_memo) <= n):
    kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]
 
gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n):
    return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0):
    gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n):
    gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]
 
def nCr(n,r):
  if(n == r):
    return 1
  if(n < r or r < 0):
    return 0
  ret = 1
  ret = ret * kaijo(n) % MOD
  ret = ret * gyaku_kaijo(r) % MOD
  ret = ret * gyaku_kaijo(n-r) % MOD
  return ret

def nPr(n,r):
  if(n < r or r < 0):
    return 0
  ret = 1
  ret = ret * kaijo(n) % MOD
  ret = ret * gyaku_kaijo(n-r) % MOD
  return ret

N,K = map(int,input().split())
lines = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    lines[a-1].append(b-1)
    lines[b-1].append(a-1)

not_visited = [-1]*N
not_visited[0] = 0
stack = deque()
stack.append(0)

ans = K
loop = 1
while stack:
    now = stack.popleft()
    c = len(lines[now])
    if loop == 1:
        ans *= nPr(K-1,c)
    else:
        ans *= nPr(K-2,c-1)
    for nex in lines[now]:
        if not_visited[nex] == -1:
            not_visited[nex] =  not_visited[now] + 1
            stack.append(nex)
    loop += 1
    ans %= MOD

print(ans)