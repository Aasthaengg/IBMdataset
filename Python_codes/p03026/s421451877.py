from collections import deque
N = int(input())
G = {k: [] for k in range(N)}
E = [0]*N
ans = [-1]*N

for _ in range(N-1):
    a, b = map(int, input().split())
    # 無向グラフ
    G[a-1].append(b-1)
    G[b-1].append(a-1)

    E[a-1] += 1
    E[b-1] += 1

C = sorted([int(i) for i in input().split()], reverse=True)
print(sum(C[1:]))


ans[E.index(max(E))] = C[0]
que = deque([(E.index(max(E)), -1)])

idx = 0
while que:
    ci, p = que.popleft()

    for ni in G[ci]:
        if ni != p:
            idx += 1
            ans[ni] = C[idx]
            que.append((ni, ci))

print(*ans)
