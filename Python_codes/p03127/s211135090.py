import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
from math import gcd

g = 0
for a in As:
    g = gcd(g, a)
print(g)