# coding: utf-8

# https://atcoder.jp/contests/abc089/tasks/abc089_d
# 17:17-18:17 read testcase
# 18:17-18:26 done


def main():
    H, W, D = map(int, input().split())
    A = [None] * H
    for i in range(H):
        A[i] = list(map(int, input().split()))
    Q = int(input())
    L, R = [None] * Q, [None] * Q
    for i in range(Q):
        L[i], R[i] = map(int, input().split())
        L[i] -= 1  # 1-index => 0-index
        R[i] -= 1  # 1-index => 0-index
    
    if D == H*W:
        for _ in range(Q):
            print(0)
        return None

    positions = [None] * (H*W)
    for i in range(H):
        for j in range(W):
            positions[A[i][j]-1] = (i, j)

    n_graph = D if D <= (H*W)//2 else (H*W)-D

    graphs = [[] for _ in range(n_graph)]

    for start in range(n_graph):
        cost = 0
        start_x, start_y = positions[start]
        m = 0
        while start + m*D < H*W:
            to_x, to_y = positions[start + m*D]
            cost += abs(to_x-start_x) + abs(to_y-start_y)
            graphs[start].append(cost)
            start_x, start_y = to_x, to_y
            m += 1

    for l, r in zip(L, R):
        graph_num = l % n_graph
        graph = graphs[graph_num]
        print(graph[r//D] - graph[l//D])


main()
# print(main())
