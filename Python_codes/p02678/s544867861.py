from collections import deque


def main():
    n, m = map(int, input().split())
    route = [[] for _ in range(n)]  # 各ノードと隣接するノード
    INF = 10 ** 12

    for _ in range(m):
        a, b = map(int, input().split())
        route[a - 1].append(b - 1)
        route[b - 1].append(a - 1)

    d = deque()
    d.append(0)
    dist = [0] + [INF] * (n - 1)  # 根からの距離
    pre = [-1] * n  # 各ノードの親

    while d:
        u = d.popleft()
        for v in route[u]:
            if dist[v] != INF:
                continue
            dist[v] = dist[u] + 1
            pre[v] = u
            d.append(v)

    print("Yes")
    for i in range(1, n):
        print(pre[i] + 1)


if __name__ == "__main__":
    main()
