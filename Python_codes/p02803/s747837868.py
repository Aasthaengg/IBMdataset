from collections import deque
h, w = map(int, input().split())
G = [list(input()) for _ in range(h)]
go = [[0,1], [1,0], [0,-1], [-1,0]]

ans = 0
# [h,w]を探索する.
for hi in range(h):
    for wi in range(w):
        # もしスタートが壁なら、各座標への距離の算出は行わない.
        if G[hi][wi] =='#':
            continue
        # BFSにより各座標への距離の算出を行う.
        ## 距離/探索したかを-1で初期化
        dist = [[-1]*w for _ in range(h)]
        ## [hi,wi]の地点の距離は0.
        dist[hi][wi] = 0
        ## 探索用のキューを初期化.
        que = deque([[hi,wi]])
        
        ## キューがなくなるまで以下を行う.
        while que:
            ### 探索する座標[nowhi,nowwi]
            nowhi, nowwi = que.pop()
            ### 探索する方向
            for dh, dw in go:
                #### 迷路からはみ出す箇所は探索しない.
                if not ((0<=nowhi+dh<=h-1) and (0<=nowwi+dw<=w-1)):
                    continue
                #### 通れない箇所は探索しない.
                if G[nowhi+dh][nowwi+dw]=='#':
                    continue
                #### 探索済みの箇所は探索しない.
                if dist[nowhi+dh][nowwi+dw]!=-1:
                    continue
                #### 探索する地点の距離は、現在の距離+1
                dist[nowhi+dh][nowwi+dw] = dist[nowhi][nowwi]+1
                #### キューに新たな探索済みの地点を追加.
                que.appendleft([nowhi+dh, nowwi+dw])
        # 答えはスタート地点を[h,w]で探索した際、最も長くなる距離.
        ans = max(ans, max([max(d) for d in dist]))
print(ans)