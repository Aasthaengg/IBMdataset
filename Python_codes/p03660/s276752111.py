import sys
sys.setrecursionlimit(10**8)
n = int(input())
ki = [[]for _ in range(n)]
dist1 = [0]*n
distN = [0]*n
def dfs1(now,last = -1):
    for next in ki[now]:
        if next == last:continue
        dist1[next] = dist1[now]+1
        dfs1(next,now)
def dfsN(now,last = -1):
    for next in ki[now]:
        if next == last:continue
        distN[next] = distN[now]+1
        dfsN(next,now)
        
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    ki[a].append(b)
    ki[b].append(a)
fs = 0
dfs1(0)
dfsN(n-1)
for i in range(n):
    if dist1[i] <= distN[i]:fs+=1
ss = n-fs
if fs > ss:print('Fennec')
else:print('Snuke')