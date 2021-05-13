from collections import deque

n,q = map(int,input().split())
qu = deque([])
time = 0
for i in range(n):
    a,b = input().split()
    qu.append([a,int(b)])

while len(qu) > 0:
    c = qu.popleft()
    if c[1] <= q:
        time += c[1]
        print(c[0],time)
    else:
        time += q
        qu.append([c[0],c[1]-q])
