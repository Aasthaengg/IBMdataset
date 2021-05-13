# m-solutions2019D - Maximum Sum of Minimum
def bfs(start: int) -> None:
    q = [start]
    nodes[start] = C.pop()
    while q:
        v = q.pop(0)
        for u in T[v]:
            if not nodes[u]:
                nodes[u] = C.pop()
                q.append(u)


def main():
    # adjacent edges should have close numbers as much as possible -> sort, bfs
    global T, C, nodes
    N, *ABC = map(int, open(0).read().split())
    AB, C = ABC[:-N], ABC[-N:]
    C.sort()
    T = [[] for _ in range(N + 1)]
    for v, u in zip(*[iter(AB)] * 2):
        T[v].append(u), T[u].append(v)
    score, nodes = sum(C) - C[-1], [0] * (N + 1)  # max of C will not be used
    for i, t in enumerate(T[1:], 1):
        if len(t) == 1:
            start = i  # start from any node with degree 1
            break
    bfs(start)
    print(score)
    print(*nodes[1:])


if __name__ == "__main__":
    main()