from collections import deque
N, K = map(int, input().split())

if N == 1:
    print(K)

G = {k: [] for k in range(N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    # 無向グラフ
    G[a].append(b)
    G[b].append(a)

mod = 10**9 + 7

ans = 1
for i in range(1, N+1):
    if len(G[i]) == 1:
        que = deque([(i, 0, 0, -1)])

        while que:
            ci, d1, d2, p = que.popleft()
            ans *= max(0, K-d1-d2)
            ans %= mod
            # print(ci, d1, d2, p, ans)

            c = 0
            for ni in G[ci]:
                if ni != p:
                    que.append((ni, 1, d1+c, ci))
                    c += 1

        print(ans)
        exit()
