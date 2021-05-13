from collections import deque
N, K = map(int, input().split())
MOD = 10 ** 9 + 7

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

ans = 1
went = [0] * (N+1)
go = deque()
go.append([1, -2])

while len(go) > 0:
    now, brother = go.popleft()
    went[now] = 1
    ans *= (K-2-brother)
    ans %= MOD

    c = 0 if now != 1 else -1
    for b in tree[now]:
        if went[b] == 0:
            go.appendleft([b, c])
            c += 1

    if ans == 0:
        break

print(ans)



