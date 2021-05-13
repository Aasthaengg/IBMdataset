import sys
from math import factorial
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
inf = float("inf") # 無限

n,k = map(int,input().split())

print(k*((k-1)**(n-1)))