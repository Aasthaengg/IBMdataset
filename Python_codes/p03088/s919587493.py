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

N = int(input())

memo = [{} for _ in range(N+1)]

def ok(last4):
    if "AGC" in last4 or "GAC" in last4 or "ACG" in last4 or last4 == "AGGC" or last4 == "ATGC" or last4 == "AGGC" or last4 == "AGTC":
        return False
    else:
        return True

def DFS(now,last3):
    if last3 in memo[now]:
        return memo[now][last3] 
    if now == N:
        return 1
    ret = 0
    for c in "AGCT":
        last4 = last3 + c
        if ok(last4):
            ret += DFS(now+1,last4[1:])
            ret %= MOD
    memo[now][last3] = ret
    return ret

print(DFS(0,"TTT"))