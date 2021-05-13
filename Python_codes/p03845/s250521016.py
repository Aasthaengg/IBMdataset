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

n = int(input())
t = list(map(int,input().split()))
sum_num = sum(t)
for _ in range(int(input())):
    p,x = map(int,input().split())
    print(sum_num - t[p-1] + x)