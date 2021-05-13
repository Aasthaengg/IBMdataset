import sys
input = sys.stdin.readline
from collections import *

def dfs(x, y):
    if x==0 and y==0:
        t[x][y] = False
        return False
    
    if x>=1:
        t[x][y] |= not dfs(x-1, y)
        
    if y>=1:
        t[x][y] |= not dfs(x, y-1)
        
    if min(x, y)>=1:
        t[x][y] |= not dfs(x-1, y-1)
   
    return t[x][y]
    
t = [[False]*7 for _ in range(7)]

for i in range(7):
    for j in range(7):
        dfs(i, j)

"""
for ti in t:
    print(*ti)
"""

N = int(input())
flag = True

for _ in range(N):
    a = int(input())
    
    if a%2==1:
        flag = False
        
if flag:
    print('second')
else:
    print('first')