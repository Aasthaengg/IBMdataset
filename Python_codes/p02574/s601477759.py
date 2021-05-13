import collections
import heapq
import math
import random
import sys
input = sys.stdin.readline
sys.setrecursionlimit(500005)
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().rstrip()

Nmax = 10**6 + 1

n = ri()
A = rl()

f = [0] * Nmax
for v in A:
    f[v] += 1
for i in range(2, Nmax//2+1):
    for j in range(i*2, Nmax, i):
        f[i] += f[j]

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

if max(f[2:]) <= 1:
    print("pairwise coprime")
else:
    x = 0
    for v in A:
        x = gcd(x, v)
    if x == 1:
        print("setwise coprime")
    else:
        print("not coprime")
