N,C,K=map(int,input().split())
from collections import deque
T=[int(input())for _ in range(N)]
T.sort()
T=deque(T)

ans=1
bus=T[0]+K
count=0
while T:
    i=T.popleft()
    if i>bus:
        bus=i+K
        ans+=1
        count=1
    elif count==C:
        bus=i+K
        ans+=1
        count=1
    else:
        count+=1
print(ans)