import sys
sys.setrecursionlimit(10 ** 9)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M, P = lr()
graph = [lr() for _ in range(M)]

def bellmanford(s, g):
    INF = 10**19
    dist = [INF] * (N+1)
    dist[s] = 0
    for i in range(2 * N):
        for a, b, c in graph:
            if dist[a] != INF and dist[b] > dist[a] - c + P:
                dist[b] = dist[a] - c + P
                if i >= N:
                    dist[b] = -float("inf")
 
    if dist[g] == -float("inf"):
        return -1
    else:
        return max(-dist[g], 0)

answer = bellmanford(1, N)
print(answer)
# 
