n, c, k = map(int, input().split())
from collections import deque

t = [int(input()) for _ in range(n)]
t.sort()
t=deque(t)

ans = 1
bus=t[0]+k
cnt = 0

while t:
    i=t.popleft()
    if i>bus:
        bus=i+k
        ans+=1
        cnt=1
    elif cnt==c:
        bus=i+k
        ans+=1
        cnt=1
    else:
        cnt+=1

print(ans)

