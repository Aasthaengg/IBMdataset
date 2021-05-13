import sys
from collections import Counter
from collections import deque
import math
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,m,Q=mp()
grid=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    l,r=mp()
    for k in range(1,l+1):
        grid[k][r]+=1

for i in range(n):
    for k in range(n):
        grid[i][k+1]+=grid[i][k]



for i in range(Q):
    p,q=mp()
    print(grid[p][q])