
import heapq

N,M = map(int, input().split())
es = [[] for _ in range(N)]

for i in range(M):
    a,b,c = map(int, input().split())
    es[a-1].append((c, b-1))
    es[b-1].append((c, a-1))

INF = float("inf")
# dp[i][j]:点iからjまでの最短距離
dp = [[INF for _ in range(N)] for _ in range(N)]

# 全点を開始点として探索
for i in range(N):
    # 同じ地点は距離0
    dp[i][i] = 0
    q = []
    # iまで0で行ける、を追加
    heapq.heappush(q,(0,i))
    while q:
        # 最短の候補を取り出す
        c,a = heapq.heappop(q)
        # 候補が最短でなければ捨てる
        if dp[i][a] < c:
            continue
        # 候補が最短になりうるならその点に繋がる辺を調べる
        for nc,b in es[a]:
            # i->b の経路について、i->a->bで行く方が今わかっているコストより小さい時
            if dp[i][b] > dp[i][a] + nc:
                dp[i][b] = dp[i][a] + nc
                # iからbまでdp[i][b]で行けるよ、を追加
                heapq.heappush(q, (dp[i][b],b))


        

ans = 0
for a in range(N):
    for c,b in es[a]:
        if dp[a][b] != c:
            ans += 1

print(ans//2)