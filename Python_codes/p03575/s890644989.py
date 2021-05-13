from collections import defaultdict


def main():
    N, M = list(map(int, input().split(' ')))
    adj_nodes = defaultdict(list)
    edges = list()
    for _ in range(M):
        a, b = list(map(int, input().split(' ')))
        a -= 1
        b -= 1
        edges.append((a, b))
        adj_nodes[a].append(b)
        adj_nodes[b].append(a)
    ans = 0
    for removed_edge in edges:
        a, b = removed_edge
        visited = [0 for _ in range(N)]
        frontier = [0]
        # dfs
        while len(frontier) > 0:
            node = frontier.pop()
            visited[node] = 1
            for next_node in adj_nodes[node]:
                if visited[next_node] == 1:
                    continue
                if (node, next_node) in [(a, b), (b, a)]:
                    continue
                frontier.append(next_node)
        if min(visited) == 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()