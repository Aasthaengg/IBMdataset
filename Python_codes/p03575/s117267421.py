import sys
from collections import deque
 
N, M = list(map(int,input().split()))
AB = [ list(map(int,input().split())) for _ in range(M)] #Nは頂点、Mは辺数、ABはつながっている部屋
 


count = 0
for sub in range(M):
    graph = [[] for _ in range(N + 1)] #本来は頂点数さえあればいいけど、添え字処理の都合でN+1個
    for i in range(len(AB)): #つながっている頂点セット
        if i == sub:
            continue
        else:
            graph[AB[i][0]].append(AB[i][1])
            graph[AB[i][1]].append(AB[i][0]) #有行グラフだとこの行はなくていい
     
    # bfs
    queue = deque([1]) #queue = 訪れるリスト 今回は1からスタート固定だけど、出発点がいろいろある場合はループ
    signposts = [0] * (N + 1) #これはこの問題特有。
    visit = []
    while queue: #訪れるリストがあるうちは繰り返す
        u = queue.popleft() #先入れ先出し、つまり幅優先。popにすれば深さ優先
        visit.append(u)
        for v in graph[u]: #頂点uにある隣接頂点をチェック
            if (v not in visit) and (v not in queue): #この問題特融だが、おとずれたチェックとしてvisitリストが必裕　おとずれていなかったらこの分岐に入る
                queue.append(v) #訪れるリストに頂点を追加

    if len(visit)!= N:
        count +=1
print(count)
