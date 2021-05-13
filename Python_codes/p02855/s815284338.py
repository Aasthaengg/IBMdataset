from collections import deque

def bfs():
    global q, t
    while q:
        a = q.popleft()
        for i in [-1, 1]:
            if 0 <= a + i < h:
                if t[a + i] == -1:
                    q.append(a + i)
                    t[a + i] = t[a]
    return

def solve():
    global ans
    for i in range(h):
        for j in range(w):
            ans[i][j] = ans[t[i]][j]
    for i in range(h):
        print(" ".join(map(str, ans[i])))
    return

h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = [[0] * w for _ in range(h)]
t = [-1] * h
x = 1
q = deque()
for i in range(h):
    cnt = 0
    for j in range(w):
        ans[i][j] = x
        if s[i][j] == "#":
            cnt += 1
            if cnt >= 2:
                x += 1
            ans[i][j] = x
    if cnt > 0:
        x += 1
        t[i] = i
        q.append(i)
bfs()
solve()