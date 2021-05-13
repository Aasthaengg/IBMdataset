from collections import deque
n=int(input())
a=list(map(int,input().split()))
d=deque(a)
tmp=[d[0]]
d.popleft()
ans=1
while d:
    t=tmp[-1]-tmp[0]
    if len(tmp)==1 or t==0:
        tmp.append(d.popleft())
    elif t>0 and d[0]>=tmp[-1]:
        tmp.append(d.popleft())
    elif t<0 and d[0]<=tmp[-1]:
        tmp.append(d.popleft())
    else:
        ans+=1
        tmp=[d.popleft()]
print(ans)