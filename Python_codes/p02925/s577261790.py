# 試合を頂点とした有向グラフを書く
# 対戦2チームを元に試合ID(頂点番号)に変換できるようにする
# 閉路があるとNGなので-1
# 閉路がない場合は最長経路が答え

import sys
readline = sys.stdin.readline

N = int(readline())

id_dic = {}
next_id = 0
def to_id(a,b):
  if a > b:
    a,b = b,a
  return id_dic[(a,b)]
def convert_to_id(a,b,next_id):
  if a > b:
    a,b = b,a
  if (a,b) not in id_dic:
    id_dic[(a,b)] = next_id
    return next_id + 1
  return next_id

G = [[] for i in range((N * (N - 1)) // 2)] # 試合グラフ
indegree = [0 for i in range((N * (N - 1)) // 2)] # 入次数
for i in range(N):
  A = list(map(int,readline().split()))
  cur = None
  for a in A:
    # i と a - 1の試合
    next_id = convert_to_id(i,a - 1,next_id)
    game = to_id(i,a - 1)
    if cur != None:
      G[cur].append(game)
      indegree[game] += 1 # 試合に対する入次数が1
    cur = game
  
done = [False for i in range((N * (N - 1)) // 2)] # 試合完了
# 各日付ごとに、入次数が0の試合から行っていく
# 入次数が0になった試合を翌日の試合リスト
stack = []
for i in range(len(indegree)):
  if indegree[i] == 0:
    stack.append(i)

if len(stack) == 0:
  print(-1)
  exit(0)
  
day = 0
while stack:
  day += 1
  nextday = []
  while stack:
    game = stack.pop()
    if done[game]: # 既に終わっている試合の場合　閉路と見なす
      print(-1)
      exit(0)
    done[game] = True
    for child in G[game]: # 翌日のゲームを探索
      indegree[child] -= 1
      if indegree[child] == 0: # 入次数が0になれば翌日試合できる
        nextday.append(child)
  stack = nextday

if sum(done) != ((N * (N - 1)) // 2):
  print(-1)
  exit(0)
print(day)