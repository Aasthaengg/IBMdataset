from collections import deque
n, m = map(int,input().split())

g = [[] for _ in range(n)]

#重み付き無向グラフ
for i in range(m):
    a, b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

q = deque([])

#訪問済みノード判定
check = [False]*n

cnt = 0

#連結成分のカウントBFS
for i in range(n):
    if check[i]:
        continue
    check[i] = True
    q.append(i)
    while q:
        v = q.popleft()
        x = g[v]
        for j in x:
            if check[j]:
                continue
            check[j] = True
            q.append(j)
    cnt += 1

print(cnt-1)