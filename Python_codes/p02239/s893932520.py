from collections import deque
INF = 1145141919810364364334
s = [None]
r = [None]

n = int(input())
for _ in range(n):
    temp = list(map(int,input().split()))
    s.append(temp[2:])
    
d = [INF] * (n+1)

d[1] = 0
q = deque()
q.append(1)

while q:
    x = q.popleft()
    for i in s[x]:
        if d[i] == INF:
            q.append(i)
            
        d[i] = min(d[x] + 1 , d[i])
        
for i in range(1,n+1):
    if d[i] == INF:
        d[i] = -1
    print(i,d[i])
