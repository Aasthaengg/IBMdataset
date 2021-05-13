# queueのライブラリをインポート
import queue
 
n,m = map(int,input().split())
# 各都市から繋がっている都市を記録
road = [[] for i in range(n)]
for i in range(m):
  a,b = map(int,input().split())
  road[a-1].append(b-1)
  road[b-1].append(a-1)
ans = 0
# まだ訪れていない都市を記録
city = set(i for i in range(n))
# まだ訪れていない都市がある間繰り返す
while len(city):
  # queueを用意する
  q = queue.Queue()
  # 初期値としてまだ訪れていない都市を入れる
  q.put(city.pop())
  # 1つのグループを全て辿る
  while not q.empty():
    x = q.get()
    for i in road[x]:
      # 既に訪れたか調べる
      if i in city:
        # 訪れていなければqueueに追加する
        q.put(i)
        # 未訪問の都市のリストから除外する
        city.discard(i)
  # まだ訪れていない都市があれば答えを増やす
  if len(city):
    ans += 1
print(ans)