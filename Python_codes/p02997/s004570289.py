N, K = map(int, input().split())

upper = (N - 1) * (N - 2) // 2
if K <= upper:
    pair = [(1, i) for i in range(2, N + 1)]
    rest = upper - K

    edge = []
    for i in range(2, N):
        for j in range(i + 1, N + 1):
            edge.append((i, j))
    pair.extend(edge[:rest])

    print(len(pair))
    for p in pair:
        print(*p)
else:
    print(-1)
