###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

N, Q = mi()

Events = []
#イベントを格納する配列
#各要素はタプルで、(s-x or t-x, 1or-1, x)が入っている
#意味は、「時間s-xもしくはt-xに出発する人が」「座標xで」
# 「1:通行止めにぶつかる -1:通行止めにぶつかりそうだったが、助かる」を表す

for _ in range(N):
  s, t, x = mi()
  #1つめの要素がマイナスになることはないので、max(0, hoge)をとる。
  #どちらもマイナスといったコーナーケースでも、「0で通行止めになり0で解除される」となってから時間0に出発する人が処理されるので、影響は出ない
#……と思っていたけど、0になるイベントが複数あると、集合への出し入れがおかしくなる（0を複数入れたあと複数回だそうとするから、無いキーを出そうとしてしまう）
#時間がマイナスでもコード上全く問題無いんだから、外した！
  Events.append((s-x, 1, x))
  Events.append((t-x, -1, x))

#イベント配列は「影響を受ける人（の出発時間）」で降順ソートする
#降順ソートなので、pop()でとっていく
from operator import itemgetter
Events = sorted(Events, key=lambda x:-x[1])
Events = sorted(Events, key=lambda x:-x[0])
#発生タイミング（x[0]）が同じイベントは、集合からのout→inでも並び替える（x[1]について降順）。
#outより先にinが行われると、集合操作がおかしくなる

#イベント配列ができたので、今度は各人について処理していく
#出力する答えはAnss配列に入れていき、最後にfor文で一気に出力する
Anss = []

#制約より、Diは最初から昇順ソートされている
Ds = [int(input()) for _ in range(Q)]

nowkeptout = set() #今通行止めになっている座標を格納するset。常に昇順ソートする
nextevent = Events.pop()  #次に見るイベント
minstop = 10**9+1
for d in Ds:
  #各ループにおいて、「未処理の人のうち、最も出発時間が早い人」がdに入る
  #ということは、時間dまでのEventsを全て処理すれば、その人がぶつかる場所が分かる
  while nextevent[0]<=d: #dを越えたら止まるし、イベントがなくなっても番兵で止まる
    a, b, c = nextevent
    if b==1: #座標xが通行止めになる
      nowkeptout.add(c)
      minstop = min(c, minstop)
    else: #座標xの通行止めが解除される
      nowkeptout.remove(c)
      if c==minstop and nowkeptout: minstop = min(nowkeptout)
      elif not nowkeptout: minstop = 10**9+1
    try: nextevent = Events.pop()
    except:
      nextevent = (10**9+1, 1, 1) #要素がなくなったらもう処理が起きないようにする
      break
  #この時点で、nowkeptoutに値が入っている場合も、入っていない場合もある
  #値が入っていれば、dはその最小値の座標で通行止めにぶつかる
  #値が入っていなければ歩き続けるので、-1にする
  if nowkeptout: Anss.append(minstop)
  else: Anss.append(-1)

for ans in Anss:
  print(ans)

