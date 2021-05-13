import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]
    exceptions = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
        exceptions.append((a-1, b-1))

    ans = 0
    for from_, to in exceptions:
        res = dfs(n, edges, exception={(from_, to), (to, from_)})
        if not res:
            ans += 1
    print(ans)


def dfs(nodes, edges, exception):
    seen = [False] * nodes
    todo = [0]
    while todo:
        node = todo.pop()
        if seen[node]:
            continue
        seen[node] = True

        for to in edges[node]:
            if (node, to) in exception:
                continue
            todo.append(to)

    return sum(seen) == nodes


if __name__ == "__main__":
    main()
