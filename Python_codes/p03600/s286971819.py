# https://atcoder.jp/contests/abc074/tasks/arc083_b

import sys
input = sys.stdin.buffer.readline

def floyd_warshall(V, dist):                                               # 動的計画法。頂点 k まで経由することが可能な場合の最短距離という部分問題を考えて、k = 0 から漸化式的に計算する
    res = 0
    for i in range(V):
        for j in range(i+1,V):
            flg = 0
            for k in range(V):
                if k==i or k==j:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    return -1
                if dist[i][j] < dist[i][k] + dist[k][j]:
                    flg += 1
                if flg == V-2:
                    res += dist[i][j]
    return res

N = int(input())

dist = [list(map(int, input().split())) for _ in range(N)]

if N ==2:
    print(dist[0][1])
else:
    print(floyd_warshall(N, dist))