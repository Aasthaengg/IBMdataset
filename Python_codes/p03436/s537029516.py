n,m = map(int,input().split())
from collections import deque
a = []
for _ in range(n):
    a.append(list(input()))

count = 0
for x in a:
    count += x.count("#")
#print(count)

b = [[-1 for i in range(m)] for i in range(n)]
#print(a)

x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]
queue = deque([[0,0]])
b[0][0] = 1
while queue:
    now = queue.popleft()
    if now == [n-1,m-1]:
        print(n * m - (b[n-1][m-1] + count))
        exit()
    a[now[0]][now[1]] = "#"
    for i in range(4):
        if 0 <= now[0] + y[i] < n and 0 <= now[1] + x[i] < m and b[now[0]+y[i]][now[1]+x[i]] == -1:
            if a[now[0]+y[i]][now[1]+x[i]] == '.':
                queue.append([now[0]+y[i],now[1]+x[i]])
                b[now[0]+y[i]][now[1]+x[i]] = b[now[0]][now[1]] + 1

print(-1)

