from collections import deque


def main():
    N, M = map(int, input().split())
    e = [[] for _ in range(N)]
    input_edges = [0]*N
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        e[u].append(v)
        input_edges[v] += 1
    queue = deque()
    dp = [-1] * N
    for i, input_edge in enumerate(input_edges):
        if input_edge == 0:
            queue.appendleft(i)
            dp[i] = 0
    topological_sorted = []
    while queue:
        v = queue.pop()
        topological_sorted.append(v)
        for other_side in e[v]:
            input_edges[other_side] -= 1
            if input_edges[other_side] == 0:
                queue.appendleft(other_side)
    for v in topological_sorted:
        for other_side in e[v]:
            dp[other_side] = max(dp[v] + 1, dp[other_side])
    print(max(dp))


if __name__ == "__main__":
    main()
