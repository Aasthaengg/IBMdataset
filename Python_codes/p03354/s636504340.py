# coding: utf-8

# https://atcoder.jp/contests/abc097/tasks/arc097_b
# 15:36-15:48 give up => hint
# 15:53-16:16　RE(recursion overflow)
# 16:16-16:43 done


def main():
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    p = [num-1 for num in p]
    x, y = [None] * M, [None] * M
    for i in range(M):
        x[i], y[i] = map(int, input().split())
        x[i] -= 1  # 0-index
        y[i] -= 1  # 0-index

    edges = {node: [] for node in range(N)}
    for xi, yi in zip(x, y):
        edges[xi].append(yi)
        edges[yi].append(xi)

    ans = 0
    check_node = [None] * N
    for start in range(N):
        if check_node[start] is not None:
            continue

        indexes = []
        numbers = []
        queue = [start]
        queue_i = 0
        while queue_i < len(queue):
            node = queue[queue_i]
            if check_node[node] is not None:
                queue_i += 1
                continue

            check_node[node] = 1
            indexes.append(node)
            numbers.append(p[node])
            
            for edge in edges[node]:
                if check_node[edge] is None:
                    queue.append(edge)
            
            queue_i += 1

        ans += len(set(indexes) & set(numbers))

    return ans


print(main())
