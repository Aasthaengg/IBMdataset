# "()"となっている部分は全て削除できる
# "("だけで構成されているものは、ポイントuP
# ")"だけで構成されているものは、ポイントDOWN(最後に使う)
# ")("で構成されているものは、")"より"("の方が多いものと少ないものと同じものに分ける
# ・")"より"("のほうが多いものを、")"の数が少ない順に使っていく
# ・")"と"("の数が同じものを使う
# ・")"より"("のほうが少ないものを、")"の数が多い順に使っていく

import sys
readline = sys.stdin.readline

N = int(readline())
opencnt = 0
closecnt = 0
open_close_up = []
open_close_equal = []
open_close_down = []
for i in range(N):
  s = readline().rstrip()
  while "()" in s:
    s = s.replace("()","")
  opn = s.count("(")
  clo = s.count(")")
  if opn == 0 and clo == 0:
    # 空文字になったので無視してよい
    continue
  if opn == 0:
    # 全てクローズの場合
    closecnt += clo
  elif clo == 0:
    # 全てオープンの場合
    opencnt += opn
  elif opn > clo: # ")(("のようなケース
    open_close_up.append([clo,opn])
  elif opn == clo:
    open_close_equal.append([clo,opn])
  elif opn < clo:
    open_close_down.append([clo,opn])

open_close_up = sorted(open_close_up,key = lambda x:x[0]) # closeの数が少ない順
open_close_down = sorted(open_close_down,key = lambda x:x[0],reverse = True) # 多い順
  
# まずオープンを全て使う
cur = opencnt

# オープンの数が増えるものを全て使う
for i in range(len(open_close_up)):
  clo,opn = open_close_up[i][0],open_close_up[i][1]
  if clo > cur:
    print("No")
    exit(0)
  cur -= clo
  cur += opn

# オープンの数が変わらないものを全て使う
for i in range(len(open_close_equal)):
  clo,opn = open_close_equal[i][0],open_close_equal[i][1]
  if clo > cur:
    print("No")
    exit(0)
    
for i in range(len(open_close_down)):
  clo,opn = open_close_down[i][0],open_close_down[i][1]
  if clo > cur:
    print("No")
    exit(0)
  cur -= clo
  cur += opn
  
if cur - closecnt == 0:
  print("Yes")
else:
  print("No")
