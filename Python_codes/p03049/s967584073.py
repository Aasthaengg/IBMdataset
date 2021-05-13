# (1)ABが含まれる個数・・・まず単純にカウント
# (2)Aで終わるけどBで始まらないものの個数
# (3)Bで始まるものAで終わらないもののの個数
# (4)Bで始まってAで終わるものの個数 の個数 - 1
# (4)が1以上ある場合、(2),(3)を一つずつ使うことでそれぞれ+1
# それでも(2)(3)のペアが作れればペアごとに+1

import sys
readline = sys.stdin.readline

N = int(readline())
ans = 0
a_end = 0
b_start = 0
a_end_b_start = 0

for i in range(N):
  s = readline().rstrip()
  ans += s.count("AB")
  if s[-1] == "A" and s[0] == "B":
    a_end_b_start += 1
  elif s[-1] == "A":
    a_end += 1
  elif s[0] == "B":
    b_start += 1

if a_end_b_start > 0:
  ans += a_end_b_start - 1
  if a_end > 0:
    a_end -= 1
    ans += 1
  if b_start > 0:
    b_start -= 1
    ans += 1

ans += min(a_end,b_start)
print(ans)