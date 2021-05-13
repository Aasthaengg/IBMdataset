# 符号が異なる数同士の引き算をすれば絶対値が大きくなる
# 基本は負から正を引いて大きな負の数を作る
# 最後だけ正から負を引いて大きな正の数を作る
# 正と正しか存在しない場合は最も小さい数からその他の数を引くことで負の数を作れる
# 負と負しか存在しない場合は最も大きい数からその他の数を引くことで正の数を作れる
# 正のリストと負のリスト両方を管理する
# 0は何も影響を与えないのでとりあえず正のリストに入れておく

N = int(input())
A = list(map(int,input().split()))

if len(A) == 2:
  x = max(A)
  y = min(A)
  print(x-y)
  print(x,y)
  exit(0)

plusA = []
minusA = []
for a in A:
  if a >= 0:
    plusA += [a]
  else:
    minusA += [a]
    
method = [] # 計算過程をメモ
if len(plusA) == 0:
  minusA = sorted(minusA) # 最も小さな数を取り出すため
#  print("minusA",minusA)
  x = minusA.pop()
  y = minusA.pop()
#  print("x",x,"y",y)
  method.append([x,y])
  plusA.append(x-y)
#  print("plusA",plusA,"minusA",minusA,"method",method)
elif len(minusA) == 0:
  plusA = sorted(plusA)[::-1] # 最も小さな数を取り出すため
  x = plusA.pop()
  y = plusA.pop()
  method.append([x,y])
  minusA.append(x-y)
  
while True:
  if len(minusA) + len(plusA) == 1:
    print(x-y)
    for m in method:
      print(*m)
    break
  if len(plusA) == 1:
    # 正の数が一つのときは、この数から残りの負の数を引いていく
    x = plusA.pop()
    y = minusA.pop()
    method.append([x,y])
    plusA.append(x-y)
  else:
    # 正の数が複数あるときは、負の数を作り続ける
    x = minusA.pop()
    y = plusA.pop()
    method.append([x,y])
    minusA.append(x-y)
