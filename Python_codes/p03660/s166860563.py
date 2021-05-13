n=int(input())
l=[[] for i in range(n)]
for i in range(n-1):
    x,y = map(int,input().split())
    x-=1
    y-=1
    l[x].append(y)
    l[y].append(x)
from collections import deque
q=deque([0])
lf=[10**100 for i in range(n)]
lf[0]=0
while q:
    p=q.popleft()
    for i in l[p]:
        if lf[p]+1<lf[i]:
            lf[i]=lf[p]+1
            q.append(i)
q=deque([n-1])
ls=[10**100 for i in range(n)]
ls[n-1]=0
while q:
    p=q.popleft()
    for i in l[p]:
        if ls[p]+1<ls[i]:
            ls[i]=ls[p]+1
            q.append(i)
s,f=0,0
for i in range(n):
    if lf[i]<=ls[i]:
        f+=1
    else:
        s+=1
if f<=s:
    print("Snuke")
else:
    print("Fennec")

        

