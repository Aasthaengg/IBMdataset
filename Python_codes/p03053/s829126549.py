from collections import deque

h, w = map(int, input().split())
cm = [[0 for j in range(w + 2)] for i in range(h + 2)]
que = deque([])
for i in range(1, h + 1):
    s = input()
    for j in range(1, w + 1):
        if s[j - 1] == ".":
            cm[i][j] = -1
        else:
            que.append(i)
            que.append(j)
ans = 0
while len(que) > 0:
    y = que.popleft()
    x = que.popleft()
    ans = cm[y][x] + 1
    if cm[y + 1][x] == -1:
        cm[y + 1][x] = ans
        que.append(y + 1)
        que.append(x)
    if cm[y - 1][x] == -1:
        cm[y - 1][x] = ans
        que.append(y - 1)
        que.append(x)
    if cm[y][x + 1] == -1:
        cm[y][x + 1] = ans
        que.append(y)
        que.append(x + 1)
    if cm[y][x - 1] == -1:
        cm[y][x - 1] = ans
        que.append(y)
        que.append(x - 1)
print(ans - 1)