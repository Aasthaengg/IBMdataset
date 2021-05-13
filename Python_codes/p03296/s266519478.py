###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

N = int(input())
As = list(mi())

ans = 0
prevcolor = 0 #左隣のスライムが何色だったか 色は1~Nなので0はダミー
nowsectionsize = 0
for a in As:
  if prevcolor != a: #もし色が違ったら
    ans += nowsectionsize//2 #左側までの区間size//2が魔法コストになる
    nowsectionsize = 1 #リセット（今の色が新しい区間になるので0でなく1）
  else: #色が同じなら
    nowsectionsize += 1 #区間が1増える
  prevcolor = a #どちらにしろ「前の色」は更新する

#ループを出た後、区間>=2なら最後のコストがかかる
ans += nowsectionsize //2

print(ans)



