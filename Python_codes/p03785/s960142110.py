# -*- coding: utf-8 -*-

from collections import deque
n,c,k = list(map(int, input().split()))
t = deque(sorted([int(input()) for _ in range(n)]))

cnt=0
bus=[]
while t:
    flg=False
    t1=t.popleft()
    if not bus:
        bus.append(t1)
        flg=True
    elif t1-bus[0]<=k and len(bus)<c:
        bus.append(t1)
        flg=True

    if len(bus)>=c or t1-bus[0]>=k:
#        print('bus=',bus)
#        print('t1=',t1)
        cnt+=1
        bus.clear()

    if not flg:
        bus.append(t1)

if bus:
    cnt+=1
    
print(cnt)