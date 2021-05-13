def main():
    N, M = map(int, input().split())
    edges = []
    m = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append([a-1, b-1])
        m[a-1][b-1] = 1
        m[b-1][a-1] = 1

    ans = 0
    for e in edges:
        m[e[0]][e[1]] = 0
        m[e[1]][e[0]] = 0
        global visited
        visited = [0] * N
        dfs(0, m)
        if sum(visited) != N:
            ans += 1
        m[e[0]][e[1]] = 1
        m[e[1]][e[0]] = 1
    print(ans)


def dfs(node, m):
    global visited
    visited[node] = 1
    for i, edge_flag in enumerate(m[node]):
        if edge_flag == 1 and visited[i] != 1:
            dfs(i, m)


if __name__ == '__main__':
    main()
