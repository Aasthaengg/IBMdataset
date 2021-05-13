import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    if (N - 1) * (N - 2) // 2 < K:
        print(-1)
        return
    else:
        edges = set()
        for i in range(2, N + 1):
            edges.add((1, i))

        cnt = (N - 1) * (N - 2) // 2
        for i in range(1, N):
            for j in range(i, N + 1):
                if i == j:
                    continue

                if cnt == K:
                    print(len(edges))
                    for a, b in edges:
                        print(a, b)
                    return

                if (i, j) not in edges:
                    cnt -= 1
                    edges.add((i, j))

        print(len(edges))
        for a, b in edges:
            print(a, b)
        return


if __name__ == "__main__":
    main()
