from collections import deque
h , w , d = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]
zahyo = [-1 for i in range(h*w+1)]
for i in range(h):
    for j in range(w):
        zahyo[a[i][j]] = (a[i][j],i,j)
ans = [-1 for i in range(h*w + 1)]
for i in range(1,h*w+1):
    if ans[i] == -1:
        ans[i] = 0
        p = deque()
        p.append(zahyo[i])
        while p:
            now , nowx , nowy = p.popleft()
            if now + d > h*w:
                break
            tugi , nexx , nexy = zahyo[now+d]
            p.append(zahyo[now+d])
            ans[tugi] = ans[now] + abs(nowx-nexx) + abs(nowy-nexy)

    else:
        continue

q = int(input())
for i in range(q):
    l , r = map(int,input().split())
    print(ans[r]-ans[l])
