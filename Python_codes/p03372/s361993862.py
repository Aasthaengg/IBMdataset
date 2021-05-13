N,C=map(int,input().split())
X=[0]*N
V=[0]*N
for i in range(N):
  X[i],V[i]=map(int,input().split())
  
# 右にいくつ、左にいくつ、を探索する方法はO(N**10)でNG
# 片方の寿司さけを固定することを考える。
# 残りの寿司を左回りにどこまで取るかは
# 「X個まで選べるとき価値が最大になるのはどの寿司か」をあらかじめ線形で計算しておく
# 引き返す場合の引き返さない場合の両パターン
# 逆回りでこれをやっておいたほうがあとあと楽っぽい。

best_sushi_noturn=[0]*(N+1) # 寿司を取らない場合もあるのでN+1
best_sushi_turn=[0]*(N+1) # 同上
bestval_noturn=0 # 引き返さない場合の最大価値
bestval_turn=0 # 引き返す場合の最大価値
valsum=0 # そこまでの累計価値
for i in range(1,N+1):
  # i個寿司を取るのときの最適な選択を返す
  # i=0のときは寿司を取らないとき
  # i=1個目の寿司にはX[N-1]を入れたい
  dist=C-X[N-i]
  valsum+=V[N-i]
  if valsum-dist>bestval_noturn:
    bestval_noturn=valsum-dist
    best_sushi_noturn[i]=bestval_noturn
  else:
    best_sushi_noturn[i]=best_sushi_noturn[i-1] # 改善しない場合はその前の値を返す
  if valsum-dist*2>bestval_turn:
    bestval_turn=valsum-dist*2
    best_sushi_turn[i]=bestval_turn
  else:
    best_sushi_turn[i]=best_sushi_turn[i-1] # 改善しない場合はその前の値を返す

# 逆回りの場合の最大価値を表す配列ができたので、正順で取る個数を決め打ちして最大価値を算出
valsum=0
# 正順で一つも取らない場合の最大価値を算出しておく
ans=best_sushi_noturn[N]
for i in range(N):
  valsum+=V[i]
  cost=X[i]
  # 正順で引き返す場合
  if valsum-cost*2+best_sushi_noturn[N-(i+1)]>ans:
    ans=valsum-cost*2+best_sushi_noturn[N-(i+1)]
  # 逆順で引き返す場合
  if valsum-cost+best_sushi_turn[N-(i+1)]>ans:
    ans=valsum-cost+best_sushi_turn[N-(i+1)]

print(ans)