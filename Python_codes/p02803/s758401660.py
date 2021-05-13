import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))


v=[[1,0],[-1,0],[0,1],[0,-1]]
h,w=mp()
grid=["#"*(w+2)]
ans=[]
for i in range(h):
    grid.append("#"+input()+"#")
grid.append("#"*(w+2))
for i in range(h*w):
    ch=[[0]*(w+2) for i in range(h+2)]
    if grid[i//w+1][i%w+1]==".":
        sx,sy=i//w+1,i%w+1
        que=deque([[sx,sy,0]])
        while len(que):
            q=que.popleft()
            ch[q[0]][q[1]]=1
            ans.append(q[2])
            for x,y in v:
                if grid[q[0]+x][q[1]+y]=="." and ch[q[0]+x][q[1]+y]==0:
                    ch[q[0]+x][q[1]+y]=1
                    que.append([q[0]+x,q[1]+y,q[2]+1])
            
print(max(ans))