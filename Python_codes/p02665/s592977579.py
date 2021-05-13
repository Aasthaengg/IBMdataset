import math


def main():
    depth = int(input())
    leaves = [int(x) for x in input().split()]

    nodes_range = [None] * (depth + 1)
    for i in range(depth, -1, -1):
        if i == depth:
            nodes_range[i] = (leaves[i], leaves[i])
            continue
        # 枝をなるべくまとめていく。
        min_nodes = math.ceil(nodes_range[i + 1][0] / 2) + leaves[i]
        # 枝が結合せず，平行に遡る感じ。
        max_nodes = nodes_range[i + 1][1] + leaves[i]
        nodes_range[i] = (min_nodes, max_nodes)

    if nodes_range[0][0] != 1:
        # 根が1を取り得ない場合は実現不可能。
        print(-1)
        return

    max_noded_tree = [0] * (depth + 1)
    for i in range(depth + 1):
        if i == 0:
            max_noded_tree[i] = 1
            continue
        max_noded_tree[i] = min(
            (max_noded_tree[i - 1] - leaves[i - 1]) * 2,
            nodes_range[i][1])
    print(sum(max_noded_tree))
    return


if __name__ == '__main__':
    main()
