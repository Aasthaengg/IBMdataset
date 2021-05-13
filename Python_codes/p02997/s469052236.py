def main():
    N, K = map(int, input().split())

    if (N - 1) * (N - 2) // 2 < K:
        print(-1)
        return

    graph = []
    for i in range(2, N + 1):
        graph.append((1, i))

    n = (N - 1) * (N - 2) // 2

    i = 2
    while K < n and i < N:
        j = i + 1
        while K < n and j < N + 1:
            graph.append((i, j))
            n -= 1
            j += 1
        i += 1

    print(len(graph))
    for p, v in graph:
        print(p, v)


main()
