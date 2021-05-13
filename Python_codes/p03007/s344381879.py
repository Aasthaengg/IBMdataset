from collections import deque

n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
p = 0
b = 0

qp = deque([])
qn = deque([])

for i in range(n):
    b += abs(a[i])
    if a[i] < 0:
        qn.append(a[i])
        p += 1
    else:
        qp.append(a[i])
if p != 0 and p != n:
    print(b)
    for i in range(n-2):
        if len(qp) >= 2:
            x = qn.popleft()
            y = qp.popleft()
            print(x,y)
            qn.append(x-y)
        else:
            x = qn.popleft()
            y = qp.popleft()
            print(y,x)
            qp.append(y-x)
    if len(qn) == 1 and len(qp) == 1:
        x = qn.popleft()
        y = qp.popleft()
        print(y,x)
    
elif p == 0:
    print(b-2*a[0])
    x = qp.popleft()
    y = qp.pop()
    print(x,y)
    qn.append(x-y)
    for i in range(n-3):
        x = qn.popleft()
        y = qp.popleft()
        print(x,y)
        qn.append(x-y)
    if len(qp) == 1 and len(qn) == 1:
        x = qn.popleft()
        y = qp.popleft()
        print(y,x)
    
else:
    print(b-2*abs(a[-1]))
    x = qn.popleft()
    y = qn.pop()
    print(y,x)
    qp.append(y-x)
    for i in range(n-3):
        x = qn.popleft()
        y = qp.popleft()
        print(y,x)
        qp.append(y-x)
    if len(qn) == 1 and len(qp) == 1:
        x = qn.popleft()
        y = qp.popleft()
        print(y,x)