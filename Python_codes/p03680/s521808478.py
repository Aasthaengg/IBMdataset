n = int(input())
a = []
for i in range(n):
    a.append(int(input()) - 1)

visited = [False] * n
f = 0
visited[f] = True
cnt = 0
while True:
    cnt += 1
    t = a[f]
    if t == 1:
        flg = True
        break
    if visited[t]:
        flg = False
        break
    visited[t] = True
    f = t
print(cnt) if flg else print(-1)