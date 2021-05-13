def d_maximum_sum_of_minimum(N, Nodes, C):
    # 根から始め、巡回した葉にCの大きなものから順に書き込んで行く。
    import sys
    sys.setrecursionlimit(10**6)

    int_list = list(sorted(C))
    graph = [[] for _ in range(N)]
    for u, v in Nodes:  # 0-basedとする
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    def traverse_tree(parent, current, ret=[0] * N):
        """各頂点にCの値が大きなもの順に書き込んでいく"""
        def dfs(p, c):
            ret[c] = int_list.pop()
            for next_edge in graph[c]:
                if next_edge != p:  # 木を「逆戻り」しない頂点だけ調べる
                    dfs(c, next_edge)
        dfs(parent, current)
        return ret
    tmp = traverse_tree(-1, 0)
    return str(sum(tmp[1:])) + '\n' + ' '.join(map(str, tmp))

N = int(input())
Nodes = [[int(i) for i in input().split()] for j in range(N - 1)]
C = [int(i) for i in input().split()]
print(d_maximum_sum_of_minimum(N, Nodes, C))
