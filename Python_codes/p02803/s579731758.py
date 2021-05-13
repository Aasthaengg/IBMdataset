# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
"""
def main():
    H, W = map(int, input().split())
    S_lsit = [input() for i in range(H)]

    INF = 401

    node_list = []
    for i in range(H):
        node_list += [(i, j) for j in range(W)]

    dist_table = [[INF for j in range(H*W)] for i in range(H*W)]
    for i in range(H*W):
        dist_table[i][i] = 0
    #print(dist_table)

    path_list = [[] for i in range(H*W)]
    for k in range(H*W):
        node = node_list[k]
        i, j = node[0], node[1]
        if i >= 1 and S_lsit[i-1][j] == ".":
            path_list[k].append((i-1)*W + j)
        if i <= H-2 and S_lsit[i+1][j] == ".":
            path_list[k].append((i+1)*W + j)
        if j >= 1 and S_lsit[i][j-1] == ".":
            path_list[k].append(i*W + j-1)
        if j <= W-2 and S_lsit[i][j+1] == ".":
            path_list[k].append(i*W + j+1)
        for next_node in path_list[k]:
            dist_table[k][next_node] = 1
    #print(path_list)

    for k in range(H*W):
        for i in range(H*W):
            for j in range(H*W):
                dist_table[i][j] = min(
                    dist_table[i][j],
                    dist_table[i][k] + dist_table[k][j]
                )
    #print(dist_table)

    max_dist = 0
    for i in range(H*W):
        if S_lsit[i//W][i%W] == ".":
            for j in range(H*W):
                if S_lsit[j//W][j%W] == ".":
                    max_dist = max(max_dist, dist_table[i][j])
    print(max_dist)

if __name__ == "__main__":
    main()

