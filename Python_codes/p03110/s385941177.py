"""
N = list(map(int,input().split()))
S = [str(input()) for _ in range(N)]
S = [list(map(int,list(input()))) for _ in range(h)] 
print(*S,sep="")
"""

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
inf = float("inf") # 無限

btc_price = 380000.0

n = int(input())
asset = 0.0
for _ in range(n):
    x,u = input().split()
    if u == "JPY":
        asset += int(x)
    else:
        asset += float(x) * btc_price
print(asset)