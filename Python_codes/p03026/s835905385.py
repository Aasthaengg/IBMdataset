from collections import deque
n = int(input())
ki = [[] for i in range(n)]
d = [0 for i in range(n)]
for i in range(n-1):
    a , b = map(lambda x: int(x)-1,input().split())
    ki[a].append(b)
    ki[b].append(a)
c = list(map(int,input().split()))
c.sort(reverse=True)
c = deque(c)
ans = 0
d[0] = c.popleft()
q = deque()
q.append(0)
while q:
    now = q.popleft()
    for i in ki[now]:
        if d[i] == 0:
            d[i] = c.popleft()
            q.append(i)
            ans += d[i]
print(ans)
print(*d)