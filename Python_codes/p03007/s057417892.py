from collections import *
n=int(input())
a=list(map(int,input().split()))
a.sort()
a=deque(a)
ans=[]
aa=a.pop()
tmp=a.popleft()
while a:
    t=a.popleft()
    if t<=0:
        ans.append((aa,t))
        aa-=t
    else:
        ans.append((tmp,t))
        tmp-=t
ans.append((aa,tmp))
print(aa-tmp)
for i in ans:
    print(i[0],i[1])