#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
ans = count = 0

h,w,k=map(int,input().split())
S=[list(input()) for i in range(h)]
color=[[0]*w for i in range(h)]
def exist(row):
    for j in range(w):
        if S[row][j]=="#":
            return True
    return False

for i in range(h):
    for j in range(w):
        if S[i][j]=="#":
            count+=1
            color[i][j]=count  

for i in range(h):
        for j in range(1,w):
            if color[i][j] == 0: color[i][j]=color[i][j-1]
                
        for j in range(w-2,-1,-1):
            if color[i][j] == 0: color[i][j]=color[i][j+1]

for i in range(1,h):
    if not exist(i):
        color[i]=color[i-1]
        
for i in range(h-2,-1,-1):
    if not exist(i):
        color[i]=color[i+1]

for ci in color:
    print(*ci)