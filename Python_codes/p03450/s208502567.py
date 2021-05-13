from collections import defaultdict, deque, Counter
import sys
input = sys.stdin.readline
INF = float("inf")


def check(g, n):
    visited = [False] * n
    dist = [INF] * n  # 最短距離を管理
    # 連結でない場合に備えて全頂点をスタートにする
    for s in range(n):
        if visited[s]:
            continue
        # 探索していなければBFSで探索開始
        que = deque([(0, s)])
        dist[s] = 0
        visited[s] = True
        while que:
            d, u = que.popleft()
            for nd, v in g[u]:
                nd += d
                if visited[v]:
                    #  すでに探索済みなら距離が一致しているか判定
                    if dist[v] != nd:
                        return False
                else:
                    # そうでなければ探索済みにしてqueに隣接頂点を追加
                    visited[v] = True
                    dist[v] = nd
                    que.append((nd, v))
    return True


def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        l, r, d = map(int, input().split())
        l -= 1
        r -= 1
        # 重み付き有向グラフ
        g[l].append((d, r))  # (重み，頂点)で管理
        g[r].append((-d, l))  # 逆方向は-をつけることで有効グラフを表現
    if check(g, n):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
