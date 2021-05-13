import math

N, K = map(int, input().split())

upper = (N-1)*(N-2) // 2
if upper < K:
    print(-1)
else:
    diff = upper - K
    edges = []
    for i in range(2, N+1):
        edges.append((1, i))
    j = 2
    while diff > 0:
        k = j + 1
        while k <= N and diff > 0:
            edges.append((j, k))
            k += 1
            diff -= 1
        j += 1
    print(len(edges))
    for e in edges:
        print(*e)

