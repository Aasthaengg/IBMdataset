from collections import deque

N = int(input())
v = list(map(int,input().split()))

v.sort()

deq = deque(v)

while len(deq) != 1:
    x = deq.popleft()
    y = deq.popleft()
    
    nx = (x+y)/2
    
    deq.appendleft(nx)

ans = deq.popleft()

print(ans)