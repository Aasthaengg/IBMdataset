# ABC 158 D
from collections import deque

S=list(input())
q=deque(S)
Q=int(input())
inv=0
for _ in [0]*Q:
    s=input()
    if s=='1':
        inv+=1
    else:
        t,f,c=s.split()
        if ((f=='1') ^ (inv%2==1)):
            q.appendleft(c)
        else:
            q.append(c)
S=[]
if inv%2:
    while q:
        S.append(q.pop())
else:
    while q:
        S.append(q.popleft())
    
print(*S,sep='')