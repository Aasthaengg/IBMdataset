def main():
    N = int(input())
    # Nが奇数(2 * M + 1)
    #    ノード n と N - n の間に枝が無く、それ以外のすべての枝があるグラフでOK。
    # Nが偶数(2 * M)
    #    ノード n と N + 1 - n の間に枝が無く、それ以外のすべての枝があるグラフでOK。
    # 両ケースとも、枝は N * (N - 1) // 2 - M = N * (N - 1) // 2 - N // 2 本。
    edges = list()
    if N % 2 == 1:
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if i + j != N:
                    edges.append((i, j))
    else:
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if i + j != N + 1:
                    edges.append((i, j))
    print(len(edges))
    for e in edges:
        print('{} {}'.format(e[0], e[1]))


if __name__ == '__main__':
    main()