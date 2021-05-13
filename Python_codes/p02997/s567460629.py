def main(N, K):
    e_max = (N - 1) * (N - 2) // 2
    if K > e_max:
        print(-1)
        return

    edge = []
    add = []
    for i in range(2, N + 1):
        edge.append((1, i))
    for i in range(2, N):
        for j in range(i + 1, N + 1):
            add.append((i, j))

    while e_max != K:
        edge.append(add.pop())
        K += 1

    print(len(edge))
    for x, y in edge:
        print(x, y)
    return


N, K = map(int, input().split())
main(N, K)