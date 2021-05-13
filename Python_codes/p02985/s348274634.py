# ABC133E - Virus Tree 2
from collections import deque


def dfs() -> int:
    cand, ret, MOD = K - 1, K, 10 ** 9 + 7
    queue, seen = deque([1]), [0] * (N + 1)
    seen[1] = 1
    while queue:
        v = queue.popleft()
        for u in G[v]:
            if not seen[u]:
                seen[u] = 1
                ret = (ret * cand) % MOD
                cand -= 1
                queue.append(u)
        cand = K - 2
    return ret


def main():
    global N, K, G
    N, K, *AB = map(int, open(0).read().split())
    G = [[] for _ in range(N + 1)]
    for v, u in zip(*[iter(AB)] * 2):
        G[v].append(u), G[u].append(v)
    ans = dfs()
    print(ans)


if __name__ == "__main__":
    main()