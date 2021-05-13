from collections import deque

def updiv(a,b):
    if a % b == 0:
        return a // b
    else:
        return a // b + 1

N,D,A = map(int,input().split())

XH = []

for i in range(N):

    x,h = map(int,input().split())
    XH.append([x,h])

XH.sort()

q = deque([])
qs = 0
ans = 0

for i in range(N):

    X = XH[i][0]
    H = XH[i][1]

 
    while len(q) > 0 and q[0][0] < X-D:
        po = q.popleft()
        qs -= po[1] * A

    if H - qs <= 0:
        continue
        
    else:
        pl = updiv(H-qs,A)
        qs += pl * A
        ans += pl
        q.append([X+D,pl])

print (ans)
        
