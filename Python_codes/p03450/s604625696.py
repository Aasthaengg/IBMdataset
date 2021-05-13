from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    l, r, d = map(int, input().split())
    G[l].append((r, -d))
    G[r].append((l, d))


MIN = -10 ** 18

lst = [MIN] * (N + 1)

que = deque()

for i in range(1, N + 1):
    if lst[i] == MIN:
        que.append(i)
        lst[i] = 0

    while que:
        tmp = que.popleft()
        for next_, d in G[tmp]:
            if lst[next_] == MIN:
                lst[next_] = lst[tmp] + d
                que.append(next_)
                continue
            
            if lst[next_] == lst[tmp] + d:
                continue
            else:
                print ('No')
                exit()

print ('Yes')
