import sys
def input():
    return sys.stdin.readline()[:-1]

s=input()
t=input()
import collections
dic={}
lim={}
mod=len(s)
for ind,i in enumerate(s):
    if i not in dic:
        dic[i] = []
        lim[i] = 0
    dic[i].append(ind)
    lim[i] += 1
now=0
cnt=0
ok = True
#print(dic)
import bisect
for i in t:
    if i not in dic:
        ok=False
        break
    ed = bisect.bisect_left(dic[i],now)
    if ed == lim[i]:
        cnt+=1
        now = dic[i][0]+1
    else:
        now = dic[i][ed]+1
    #print(now)
if ok==True:
    print(mod*cnt+now)
else:
    print(-1)
