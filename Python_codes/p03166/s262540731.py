import sys
import collections
# input処理を高速化する
input = sys.stdin.readline
def main():
    # 入力
    N, M = map(int, input().split())
    # 隣接関係は隣接リストで管理する
    lst_edge = [[] for _ in range(N)]
    # 各頂点の入力辺の本数
    deg = [0] * N
    for _ in range(M):
        x, y = map(int, input().split())
        # 最初のindexをゼロにする
        lst_edge[x-1].append(y-1)
        deg[y-1] += 1
    # 入力辺を持たない頂点をqueueに入れる
    que = collections.deque()
    for v in range(N):
        if deg[v] == 0:
            que.append(v)
    # 各頂点の最初に入力辺を持たなかった点からの距離
    dp = [0] * N
    # For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
    # https://www.python.org/dev/peps/pep-0008/#programming-recommendations
    while que:
        v = que.popleft()
        lst_nv = lst_edge[v]
        for nv in lst_nv:
            # エッジ(v, nv)をグラフから削除する
            deg[nv] -= 1
            if deg[nv] == 0:
                # エッジがなくなったことで、入力辺がなくなったらqueueに入れる
                que.append(nv)
                # 最初に入力辺を持たなかった点からの距離
                dp[nv] = max(dp[nv], dp[v] + 1)
    print(max(dp))
main()