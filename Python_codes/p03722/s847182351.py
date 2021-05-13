N, M = map(int, input().split())
E1 = [[] for _ in range(N)]
E2 = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    E1[a-1].append((b-1, -c))
    E2[b-1].append((a-1, -c))

def bellman_ford(n, E, s=0):
    D = [1<<100] * n
    D[s] = 0
    f = 1
    k = 0
    while f:
        f = 0
        for i in range(n):
            for j, c in E[i]:
                if D[i] < 1<<100 and D[j] > D[i] + c:
                    D[j] = D[i] + c
                    f = 1
                    if k == N-1 and j == N-1: return (1, [])
        k += 1
        if k == N: return (0, D)
    return (0, D)

b, d = bellman_ford(N, E1)
if b:
    print("inf")
else:
    print(-d[-1])
