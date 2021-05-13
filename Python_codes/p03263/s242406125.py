import sys
from collections import Counter
from collections import deque
import math
import fractions
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

h,w=mp()
g=[lmp() for i in range(h)]
step=[]
for i in range(h):
    if i%2==0:
        for k in range(w):
            step.append([i,k])
    else:
        for k in range(w):
            step.append([i,w-k-1])
ans=[]
for i in range(len(step)-1):
    if g[step[i][0]][step[i][1]]%2==1:
        g[step[i][0]][step[i][1]]-=1
        g[step[i+1][0]][step[i+1][1]]+=1
        ans.append([step[i][0]+1,step[i][1]+1,step[i+1][0]+1,step[i+1][1]+1])
print(len(ans))
for a in ans:
    print(*a)