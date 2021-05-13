import sys
input = sys.stdin.readline
from collections import *
from bisect import *

s = input()[:-1]
t = input()[:-1]
idx = defaultdict(list)

for i in range(len(s)):
    idx[s[i]].append(i)

now = -1
cnt = 0

for i in range(len(t)):
    if t[i] not in idx:
        print(-1)
        exit()
        
    mark = bisect_right(idx[t[i]], now)
    
    if mark==len(idx[t[i]]):
        now = idx[t[i]][0]
        cnt += 1
    else:
        now = idx[t[i]][mark]
    
print(len(s)*cnt+now+1)