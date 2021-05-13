from collections import deque


def nearlist(N, LIST):  # 隣接リスト
    NEAR = [set() for _ in range(N)]
    COST = {}
    for a, b, c in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
        COST[(a - 1, b - 1)] = c
        COST[(b - 1, a - 1)] = c
    return NEAR, COST


def bfs(NEAR, S, N):  # 幅優先探索  # キュー
    DIST = [-1 for _ in range(N)]  # 前処理
    DIST[S] = 0
    que, frag = deque([S]), set([S])

    while len(que) > 0:
        q = que.popleft()
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            DIST[i] = DIST[q] + cost[(q, i)]
            que.append(i), frag.add(i)
    return DIST


n = int(input())
abc = [list(map(int, input().split())) for _ in range(n - 1)]
q, k = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(q)]

near, cost = nearlist(n, abc)
dist = bfs(near, k - 1, n)
for x, y in xy:
    print(dist[x - 1] + dist[y - 1])
