from collections import deque
N, M = map(int, input().split())
X = [[] for _ in range(N)]
for _ in range(M):
    l, r, d = map(int, input().split())
    X[l-1].append((r-1, d))
    X[r-1].append((l-1, -d))

done = [0] * N
dist = [0] * N
def BFS(i):
    Q = deque([i])
    done[i] = 1
    while Q:
        x = Q.popleft()
        for y, d in X[x]:
            if done[y]:
                if dist[y] != dist[x] + d:
                    return 0
            else:
                done[y] = 1
                dist[y] = dist[x] + d
                Q.append(y)
    return 1

for i in range(N):
    if done[i] == 0:
        if BFS(i) == 0:
            print("No")
            break
else:
    print("Yes")