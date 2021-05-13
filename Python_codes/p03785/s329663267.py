from collections import deque
n,c,k=map(int,input().split())
t=deque(sorted([int(input()) for i in range(n)]))
b=[]
b.append(t.popleft())
ans=0
while t:
    if len(b)==c or t[0]>b[0]+k:
        ans+=1
        b=[]
    b.append(t.popleft())
if len(b)>0:
    ans+=1
print(ans)