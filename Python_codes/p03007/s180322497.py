###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

N = int(input())
As = list(mi())

TL = [[], [], []]
#[0] : zeroList
#[1] : minusList
#[2] : plusList

for a in As:
  if a == 0: TL[0].append(a)
  elif a < 0: TL[1].append(a)
  else: TL[2].append(a)

#print(TL)

ans = 0
printlist = []
#全てxxの場合（3パターン）
if len(TL[0])==N: #全てゼロの場合
  print(0)
  for i in range(N-1):
    print(0, 0)
  exit()
elif len(TL[1])==N: #全てminusの場合
  TL[1] = sorted(TL[1], reverse=True) #降順に並べる（-値の低いものから）
  printlist.append((TL[1][0],TL[1][1])) #痛みを最小に
  hand = TL[1][0]-TL[1][1] #これでプラスになった
  idx = 2
  while idx < N:
    printlist.append((hand, TL[1][idx]))
    hand -= TL[1][idx]
    idx += 1
  ans = hand
  #答えを出力する
  print(ans)
  for x, y in printlist:
    print(x, y)
  exit()
elif len(TL[2])==N: #全てplusの場合
  TL[2] = sorted(TL[2]) #昇順に並べる
  printlist.append((TL[2][0],TL[2][1])) #痛みを最小に
  hand = TL[2][0]-TL[2][1] #これで-になった
  idx = 2
  while idx < N-1:
    printlist.append((hand, TL[2][idx]))
    hand -= TL[2][idx]
    idx += 1
  #idx==N-1
  printlist.append((TL[2][idx], hand))
  hand = TL[2][idx]-hand
  ans = hand
  #答えを出力する
  print(ans)
  for x, y in printlist:
    print(x, y)
  exit()

# ここから先は、0,-,+のうちどれか2つはあるので、全て集合させられる
# ただし、0と-が1つずつ、0と+が1つずつというパターンは別途処理する必要がある
# 以下、そのパターンを処理
if len(TL[0])==1 and len(TL[1])==1:
  #0と-が1つずつ。0から-を引いて終わり
  left, right = TL[0].pop(), TL[1].pop()
  print(left-right)
  print(left, right)
  exit()
elif len(TL[0])==1 and len(TL[2])==1:
  #0と+が1つずつ。+から0を引いて終わり
  left, right = TL[2].pop(), TL[0].pop()
  print(left-right)
  print(left, right)
  exit()

# ここから先は、0,-,+のうちどれか2つはあり、前述のパターンも無いので、全て集合させられるし、最後に-と+が1つずつという最終処理パターンに持っていける
# よって一律のループ処理でOK
# 0が0個、+が1つ、-が1つになったら処理を抜け、最終手順に向かう
# 最初からそうなら、while文は実行されないのでＯＫ
# また、全てを集合させられる＝取り出す順番はどうでもいいので、高速化のため全てpop()で取り出していく
while not (len(TL[0])==0 and len(TL[1])==1 and len(TL[2])==1):
  left = 0
  right = 0
  if len(TL[0])>=1:
    #0があれば、まず0を消化する
    if len(TL[1])==0: #-がなければ、0を使って-を作る
      left, right = TL[0].pop(), TL[2].pop()
      printlist.append((left, right))
      TL[1].append(left-right)
    elif len(TL[2])==0: #+がなければ、0を使って+を作る
      left, right = TL[0].pop(), TL[1].pop()
      printlist.append((left, right))
      TL[2].append(left-right)
    else: #-も+もあるなら消化するだけなので、どっちでもいいが、-で消化する
      left, right = TL[1].pop(), TL[0].pop()
      printlist.append((left, right))
      TL[1].append(left-right)
    continue
  #ここからは、0がなくなったパターン
  #0がなくなったということは、+と-は必ず両方あることになる
  #またwhile文の条件から、「どちらも1つしかない」ということはありえない
  if len(TL[1])>=len(TL[2]): #-のが多い、もしくは同じ（もちろん2:2以上）
    left, right = TL[2].pop(), TL[1].pop()
    printlist.append((left, right))
    TL[2].append(left-right)
  else: #+のが多いパターン
    left, right = TL[1].pop(), TL[2].pop()
    printlist.append((left, right))
    TL[1].append(left-right)

# 最後に、プラス-マイナスでプラス数字を作って終わり
left, right = TL[2].pop(), TL[1].pop()
printlist.append((left, right))
ans = left-right


#答えを出力する
print(ans)
for x, y in printlist:
  print(x, y)

