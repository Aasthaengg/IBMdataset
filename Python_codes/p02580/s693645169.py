H, W, M = map(int, input().split())

#方針
# 1,基本的には、行和の最大と列和の最大の和が答えとなる
# 2,例外として、行和の最大を与える行と、列和の最大を与える列との交差点が、
#   全て爆破対象で埋まっている場合(飽和)、重複分の1を引く必要がある。

A = [0 for _ in range(H)] # 各行の爆破対象の個数 (行和)
B = [0 for _ in range(W)] # 各列の爆破対象の個数 (列和)
C = set() # 爆破対象の位置の集合

for _ in range(M): #入力処理
  h, w = map(int, input().split())
  A[h-1] += 1
  B[w-1] += 1
  C.add((h-1, w-1))

# 処理1, 行和の最大と列和の最大の和を求める
d = max(A) # 行和の最大
e = max(B) # 列和の最大
ans = d+e # 爆破できる最大の個数(仮)

# 処理2, 飽和を検出する
#  方針: 「交差点個数 == 交差点上の対象物個数」 なら飽和とする

F = set() # 最大を与える行の集合
G = set() # 最大を与える列の集合
for h in range(H):
  if A[h] == d:
    F.add(h)
for w in range(W):
  if B[w] == e:
    G.add(w)
  
spot = len(F)*len(G) # 最大を与える列と、最大を与える行の交差点の個数
bm_on_spot = 0 # 上記交差点の上にある対象物の個数 (以下のループ中でカウントする)
for c in C:
  if c[0] in F and c[1] in G: # 対象物が交差点上にある場合,カウント+1
    bm_on_spot += 1
    
if bm_on_spot == spot: #「交差点個数 == 交差点上の対象物個数」 なら飽和とする
  ans -= 1

print(ans)