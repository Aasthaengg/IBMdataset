# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
49min 40sec
"""
# 0番目の頂点から各頂点までの距離を求めて、
# その距離の偶奇を判定すればよいだろう。
# 木だから頂点同士の距離は1通りしかない。

def main():
    N = int(input())
    edge_list = [list(map(int, input().split()))  for i in range(N-1)]

    # 頂点uから頂点vに距離wの辺があることを、
    # 隣接リストadj_listのu番目の要素に[v, w]があることとして書く。
    # 今距離wは偶奇しか興味が無いので、w%2に置き換える。
    # 頂点の番号は、入力では1インデックスなので、0インデックスに変える。
    # 無向グラフなので、両向きとも入力する。
    adj_list = [[] for i in range(N)]
    for edge in edge_list:
        adj_list[edge[0]-1].append([edge[1]-1, edge[2]%2])
        adj_list[edge[1]-1].append([edge[0]-1, edge[2]%2])

    # 各頂点の頂点0からの距離のリスト
    INF = 2
    distance_list = [ INF for i in range(N)]
    distance_list[0] = 0

    # dfsのためのスタック
    dfs_list = [0]

    # dfs
    while dfs_list:
        now_node = dfs_list.pop(-1)
        now_dist = distance_list[now_node]
        for edge in adj_list[now_node]:
            if distance_list[edge[0]] == INF:
                distance_list[edge[0]] = (now_dist+edge[1])%2
                dfs_list.append(edge[0])
    
    # 答えの出力
    for dist in distance_list:
        print(dist)
    return

if __name__ == "__main__":
    main()

