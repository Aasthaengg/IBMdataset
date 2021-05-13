import sys
sys.setrecursionlimit(10 ** 6)
import sys
N,Q = map(int,input().split())
graph = [[] for _ in range(N)]
#グラフをリストで表現
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)#リストの番号で頂点を表示するため-1
    graph[b-1].append(a-1)
point = [0]*N
for _ in range(Q):
    a,b = map(int,input().split())
    point[a-1] += b#根にあたる部分にだけコストをプラス


#再帰定義
def dfs(now, prev = -1):#prev,now,nextの三段階を扱う
    for next in graph[now]:#今見ている頂点に連結されているものを見る
        if next == prev:#親だったら飛ばす
            continue
        point[next] += point[now]#子の得点をプラス
        dfs(next,now)#nextが親だけになると自分を呼ぶ前に飛ばされて終わる

dfs(0)#根頂点を指定してスタート
print(*point)