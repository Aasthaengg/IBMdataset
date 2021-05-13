temparr = input()
from heapq import heappush, heappop

import sys
x=150000
sys.setrecursionlimit(x)
temparr = temparr.split()
n = int(temparr[0])
edg = int(temparr[1])
dicts = {}
secdict = {}
firstdict = {}
for e in range(edg):
    temparr = input()
    temparr = temparr.split()
    edgearr = []
    for i in temparr:
        edgearr.append(int(i))
    first = int(edgearr[0])
    sec = int(edgearr[1])
    if first not in dicts:
        dicts[first] = []
    dicts[first].append(sec)
    if first not in firstdict:
        firstdict[first] = 1 
tail = []
ans = {}

for i in range(1, n + 1):
    if i not in firstdict:
        tail.append(i)
        ans[i] = 0
        
def dfs(node):
    global ans, dicts
    if node in ans:
        return ans[node]
    if node not in  dicts:
        return 0  
    best = 0 
    for neigh in dicts[node]:
        curnew = dfs(neigh) + 1
        if curnew > best:
            best = curnew
    ans[node] = best 
    return best
ans2 = 0 
for i in range(1, n + 1):
    ans2 = max(dfs(i), ans2)
print(ans2)
