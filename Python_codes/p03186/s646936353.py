###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

A, B, C = mi()

ans = 0

#もし解毒剤入りが毒入り-1あったら全部食べられる
if A+B >= C-1:
  print(B+C)
  exit()

#足りなかったら
#Bの数だけ、BとCを食べ続けて解毒状態を保てる → B*2
#残ったCよりBのが多いので、毒入りクッキーをBの数だけ食べて解毒し、最後に1枚食べてお腹を壊したまま終わればいい
print((B*2) + A + 1)


