import sys;sys.setrecursionlimit(10**6)
from collections import*
n=int(input())
d=defaultdict(list)

start=float("inf")
for i in range(n-1):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
    start=min(a,start)
p=sorted(map(int,input().split()))

def DFS(point,TFlist):
    global ans
    global score
    if all(TFlist):
        return 1
    for i in d[point]:
        if TFlist[i-1]:
            continue
        TFlist[i-1]=True
        tmp=p.pop()
        ans[i-1]=tmp
        score.append(tmp)
        #print(score)
        DFS(i,TFlist)
        TFlist[i-1]=False
    return score,ans

TFlist=[False]*(n)
TFlist[start-1]=True
ans=[0 for i in range(n)]
score=[]
ans[start-1]=p.pop()
s,t=DFS(start,TFlist)
#print(d)
print(sum(s))
print(*t)