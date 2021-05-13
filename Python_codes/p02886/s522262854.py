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
d = list(map(int,input().split()))


answer = 0
for i in range(n):
    temp=0
    for j in range(i+1,n):
        temp+=d[j]
    answer+=d[i]*temp

print(answer)