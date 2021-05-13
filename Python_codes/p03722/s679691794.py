# coding:utf-8
from pprint import pprint


def bellman_ford(V, E, s):
    """ 始点sから残りのノードへの最短経路を求めるベルマンフォード法
    :param V: 頂点数
    :param E: (ノード1, ノード2, コスト)のタプルのリスト
    :param s: 始点とするノード
    :return : (距離リスト, 最短経路, 負の辺によるループが存在するか)a
    """
    ##### 前処理 #####
    from collections import defaultdict
    # INFの定義
    INF = 2**63 - 1
    # 最短経路情報を格納する辞書
    dist = defaultdict(lambda: INF) # 始点から始点への移動コスト
    dist[s] = 0
    # 移動経路の履歴
    pre = {}

    ##### 最短経路算出 #####
    # 高々|V|-1回の探索でいい(|V|回以上更新がある場合は負の閉路が存在)
    for i in range(V-1):
        for n1, n2, w in E:
            # 始点からi回の探索でたどり着けない頂点は考慮しない
            # 始点 -> n2 までの最短距離 > 始点 -> n1 までの最短距離 + n1 -> n2 への移動コスト
            # の場合より短い経路が発見できたと言うことなので情報を更新
            if dist[n1] != INF and dist[n2] > dist[n1] + w:
                dist[n2] = dist[n1] + w
                pre[n2] = n1

    ##### 負の閉路検出 #####
    is_cycle = False
    cycle_node = []
    for n1, n2, w in E:
        # 正しい最短距離が求まったと仮定(重要)
        # 始点 -> n1 までの最短距離 + n1 -> n2 への移動コスト < 始点 -> n2 までの最短経路
        if dist[n1] + w < dist[n2]:
            is_cycle = True
            cycle_node.append(n1)

    ##### Infか判定 #####
    is_inf = False
    if is_cycle:
        route_node = V
        while route_node != s:
            route_node = pre[route_node]
            if route_node in cycle_node:
                is_inf = True
                break

    return 'inf' if is_inf else str(-dist[V])


def main():
    # 頂点，辺の数
    N, M = map(int, input().split(' '))
    # 辺の情報
    E = []
    for _ in range(M):
        a, b, c = map(int, input().split(' '))
        E.append((a, b, -c))

    print(bellman_ford(N, E, 1))


if __name__ == '__main__':
    main()
