import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

from math import ceil
a, b = mapint()
print(ceil((a+b)/2))