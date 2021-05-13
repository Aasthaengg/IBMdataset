# ABC133E - Virus Tree 2
from collections import deque


def main():
    N, K, *AB = map(int, open(0).read().split())
    MOD = 10 ** 9 + 7
    G = [[] for _ in range(N + 1)]
    for v, u in zip(*[iter(AB)] * 2):
        G[v].append(u), G[u].append(v)
    queue = deque([1])
    seen = [0] * (N + 1)
    seen[1] = 1
    ans, cand = K, K - 1
    while queue:
        v = queue.popleft()
        for u in G[v]:
            if not seen[u]:
                seen[u] = 1
                ans = (ans * cand) % MOD
                cand -= 1
                queue.append(u)
        cand = K - 2
    print(ans)


if __name__ == "__main__":
    main()