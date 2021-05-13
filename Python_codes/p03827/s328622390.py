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
s = input()
count = 0
max_num = 0
for _ in s:
    if _=="I":
        count+=1
    else:
        count-=1
    if max_num<count:
        max_num=count
print(max_num)