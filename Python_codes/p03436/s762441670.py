from collections import deque
h, w = map(int, input().split())
chiz = [[] for _ in range(w)]
cnt = 0
for _ in range(h):
    tmp_list = input()
    for i in range(w):
        if tmp_list[i]=='.':
            cnt += 1
        chiz[i].append(tmp_list[i])
dq = deque([(0,0)])
chiz[0][0] = 0
while dq:
    i,j = dq.popleft()
    for e in [(1,0),(-1,0),(0,-1),(0,1)]:
        if i+e[0]>=0 and i+e[0]<w and j+e[1]>=0 and j+e[1]<h:
            if chiz[i+e[0]][j+e[1]] == '.':
                chiz[i+e[0]][j+e[1]] = chiz[i][j] + 1
                dq.append((i+e[0],j+e[1]))
try:
    print(cnt-chiz[w-1][h-1]-1)
except:
    print(-1)