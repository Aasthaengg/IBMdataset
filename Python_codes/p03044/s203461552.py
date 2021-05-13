from collections import deque
n = int(input())
trees = [[] for _ in range(n)]

for i in range(n-1):
    a, b, w = map(int, input().split())
    trees[a-1].append([b-1, w])
    trees[b-1].append([a-1, w])

color = [0 for _ in range(n)]
visited = set()

next = deque()
next.append(0)
visited.add(0)
color[0] = 1

while len(next):
    i = next.popleft()
    for j, d in trees[i]:
        if j in visited:
           continue
        if d % 2 == 0:
            color[j] = color[i]
        else:
            color[j] = color[i] * -1
        next.append(j)
        visited.add(j)

for i in color:
    if i == -1:
        print(0)
    else:
        print(i)