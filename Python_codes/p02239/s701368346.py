from collections import deque

n = int(input())
m = [[0 for j in range(n)] for i in range(n)]
color = [0 for i in range(n)]
q = deque()
dist = [-1 for i in range(n)]


def bfs(s):
    color[s], dist[s] = 1, 0
    q.append(s)

    while len(q) != 0:
        u = q.popleft()
        for v in range(n):
            if m[u][v] == 1 and color[v] == 0:
                color[v], dist[v] = 1, dist[u] + 1
                q.append(v)

        color[u] = 2


def main():
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(2, len(data)):
            m[data[0]-1][data[j]-1] = 1

    bfs(0)

    for i in range(n):
        print(i+1, dist[i])


if __name__ == '__main__':
    main()

