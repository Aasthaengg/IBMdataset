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

h,w = map(int,input().split())
for _ in range(h):
    temp = input()
    for __ in range(2):
        print(temp)