from collections import defaultdict, deque

int1 = lambda x: int(x) - 1


def topological_sort(N, G):
    outs = defaultdict(list)
    ins = defaultdict(int)
    for v1, v2 in G:
        outs[v1].append(v2)
        ins[v2] += 1

    q = deque(v1 for v1 in range(N) if ins[v1] == 0)
    while q:
        v1 = q.popleft()
        yield v1
        for v2 in outs[v1]:
            ins[v2] -= 1
            if ins[v2] == 0:
                q.append(v2)


N, M = map(int, input().split())
G = [tuple(map(int1, input().split())) for _ in range(M)]
dp = [-1] * (N + 1)  # dp[N]は親がいないときの処理用

parents = [[N] for _ in range(N)]
for v1, v2 in G:
    parents[v2].append(v1)
for x in topological_sort(N, G):
    dp[x] = max(dp[p] for p in parents[x]) + 1
print(max(dp))
