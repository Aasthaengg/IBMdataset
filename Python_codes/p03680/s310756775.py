N = int(input())
As = [int(input()) for i in range(N)]
visited=[False]*N
c = 0
now = 0
while True:
    if visited[now]:
        c = -1
        break
    visited[now] = True
    c+=1
    now = As[now]-1
    if now == 1:
        break
print(c)