import math  # noqa
import bisect  # noqa
import queue  # noqa


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [[s for s in input()] for _ in range(H)]

    INF = 1000000005
    traj = [[INF for _ in range(W)] for _ in range(H)]
    que = queue.Queue()
    que.put((0, 0))
    traj[0][0] = 0 if S[0][0] == '.' else 1
    while not que.empty():
        h, w = que.get()
        d = ((0, 1), (1, 0))
        for dh, dw in d:
            nh = h + dh
            nw = w + dw
            if nh < 0 or H <= nh or nw < 0 or W <= nw:
                continue
            cost = traj[h][w]
            if S[h][w] == '.' and S[nh][nw] == '#':
                cost += 1
            if cost < traj[nh][nw]:
                traj[nh][nw] = cost
                que.put((nh, nw))

    print(traj[-1][-1])
