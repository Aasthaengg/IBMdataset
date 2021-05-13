from collections import deque


def main():
    N, M = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(M)]

    G = [[] for _ in range(N)]
    ins = [0] * N
    for i in range(M):
        G[xy[i][0] - 1].append(xy[i][1] - 1)
        ins[xy[i][1] - 1] += 1

    DP = [0] * N
    queue = deque()
    for i in range(N):
        if ins[i] == 0:
            queue.append(i)

    while queue:
        v = queue.popleft()
        for i in G[v]:
            ins[i] -= 1
            if ins[i] == 0:
                DP[i] = max(DP[i], DP[v] + 1)
                queue.append(i)

    print(max(DP))


if __name__ == '__main__':
    main()

exit()
