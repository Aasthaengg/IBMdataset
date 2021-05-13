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

a=int(input())
b=int(input())
c=int(input())

amount = int(input())

count = 0
for i in range(a+1):
    for j in range(b+1):
        temp = amount - (500*i + 100*j)
        
        if temp < 0:
            continue
        elif temp%50!=0:
            continue
        elif c < temp//50:
            continue
        # print(temp)
        count+=1
print(count)