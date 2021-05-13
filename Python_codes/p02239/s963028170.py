from collections import deque
n = int(input())
data = [None]*n
for _ in range(n):
    a,*b = map(int,input().split())
    a -= 1
    data[a] = [i-1 for i in b[1:]]
d = [-1]*n
dq = deque([(0,0)])
while dq:
    p,q = dq.popleft()
    if d[p] == -1:
        d[p] = q
        for i in data[p]:
            dq.append((i,q+1))
for i,j in enumerate(d):
    print(i+1,j)
