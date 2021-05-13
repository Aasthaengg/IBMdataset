from collections import deque

mod = 10 ** 9 + 7

N, K, *AB = map(int, open(0).read().split())

E = [set() for _ in range(N + 1)]
for a, b in zip(*[iter(AB)] * 2):
    E[a].add(b)
    E[b].add(a)

ans = K

Q = deque([1])
while Q:
    v = Q.popleft()
    for i, u in enumerate(E[v], 1):
        ans *= (K - i - (v > 1))
        ans %= mod
        E[u].remove(v)
        Q.append(u)

print(ans)