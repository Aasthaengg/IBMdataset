from collections import deque


N, X, Y = map(int, input().split())
to = [[] for _ in range(N)]

for i in range(N - 1):
    to[i].append(i + 1)
    to[i + 1].append(i)

X, Y = X - 1, Y - 1
to[X].append(Y)
to[Y].append(X)


def main():
    ans = [0] * N
    for i in range(N):
        dist = [-1] * N
        dist[i] = 0
        que = deque([i])

        while que:
            v = que.popleft()
            for nv in to[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    if nv > i:
                        ans[dist[nv]] += 1
                    que.append(nv)

    print(*ans[1:], sep='\n')


if __name__ == "__main__":
    main()