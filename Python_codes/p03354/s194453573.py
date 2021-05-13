from collections import deque

N,M = map(int,input().split())

p = list(map(int,input().split()))

for i in range(N):
    p[i] -= 1

data = [[] for i in range(N)]

for i in range(M):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    data[x].append(y)
    data[y].append(x)

group = [0] * N
count = 1
for i in range(N):
    if group[i] != 0:
        continue
    group[i] = count
    stack = deque([[i,i]])
    while stack:
        x = stack.pop()
        for y in data[x[1]]:
            if y == x[0] or group[y] != 0:
                continue
            stack.append([x[1],y])
            group[y] = count
    count += 1

#print(group)

p_inv = [0] * N

for i in range(N):
    p_inv[p[i]] = i

ans = 0

for i in range(N):
    if group[i] == group[p_inv[i]]:
        ans += 1

print(ans)


