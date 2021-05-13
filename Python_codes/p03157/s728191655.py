h,w = map(int, input().split())
l = [None]*h
for i in range(h):
    l[i] = list(input())

from collections import deque
b_Q = deque()
for i in range(h):
    for j in range(w):
      if l[i][j]=="#":
          b_Q.append([i,j])

ans=0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited=[[0 for i in range(w)] for j in range(h)]
while b_Q:
    p = b_Q.popleft()
    now = l[p[0]][p[1]]

    if visited[p[0]][p[1]] == 1:
        continue
    visited[p[0]][p[1]] = 1
    b_cnt=1
    w_cnt=0

    search_Q = deque()
    search_Q.append([p[0],p[1]])

    while search_Q:
        sch = search_Q.popleft()
        current = l[sch[0]][sch[1]]
        for i in range(4):
            nx = sch[1] + dx[i]
            ny = sch[0] + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if current != l[ny][nx] and visited[ny][nx] == 0: # b->w or w->b
                    if current=="#":
                        w_cnt+=1
                    else:
                        b_cnt+=1
                    search_Q.append([ny,nx])
                    visited[ny][nx]=1
    ans+= b_cnt*w_cnt
print(ans)