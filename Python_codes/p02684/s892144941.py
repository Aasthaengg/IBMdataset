N, K = map(int, input().split())
A = list(map(int, input().split()))

A.insert(0,0)

start = 1
next_ = A[1]

visited = [0] * (N+1)
visited[start] = 1

route = [1]
cnt = 0
while True:
    if visited[next_] == 1:
        break
    visited[next_] = 1
    route.append(next_)
    cnt += 1
    if cnt >= K:
        print(next_)
        exit()
    next_ = A[next_]

roop_s = route.index(next_)
roop = route[roop_s:]

stop = (K - roop_s) % len(roop) + 1
ans = roop[stop-1]

print(ans)
