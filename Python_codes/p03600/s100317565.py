# https://atcoder.jp/contests/abc074/tasks/arc083_b
# DP
import copy
import sys
input = sys.stdin.readline
n = int(input()) # 入力が1つ
# map(int, input().split()) # 入力が複数
graph = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    graph.append(row)

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                # iからjに行く間に、kを挟む方が早いパターンが存在するなら、最短ではない。
                print(-1)
                exit()
            elif graph[i][j] == graph[i][k] + graph[k][j] and k != i and k != j:
                # 自分の点以外で、iからjに行く間に、kを挟んでも同じパターンが存在するなら、それは不要。
                break
        else:
            ans += graph[i][j]

print(ans // 2)
