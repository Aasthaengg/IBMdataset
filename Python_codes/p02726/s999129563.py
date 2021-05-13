# BFS

n, x, y = (map(int, input().split()))

pic = [[] for _ in range(n+1)] #[]:dummy
for _ in range(1,n):
    pic[_].append(_+1)
    pic[_+1].append(_)
pic[x].append(y)
pic[y].append(x)
#print(pic)

ptns = [0 for _ in range(n)] # 0:dummy

from collections import deque

for i in range(1,n+1): #'i'を開始位置として各頂点までの最短距離を探索
    queue = deque([i]) # dequeオブジェクト、初期値は開始位置の'i'のみ
    dis = [None] * (n+1) # 'i'からの最短距離を初期化, 0:dummy含む
    dis[i] = 0 # 開始位置なので'0'
    
    while queue:
        v = queue.popleft() # v:探索元のノード 
        for j in pic[v]: # pic[v]: 探索元のノードに隣接するノード
            if dis[j] is None:
                dis[j] = dis[v] + 1
                queue.append(j)
    #print(dis)
    for k in dis[1:]: # 最短距離を集約
        ptns[k] += 1

for l in ptns[1:]: # 1以上の最短距離を出力
    print(l//2) # 往復分が記録されているため2で割る
