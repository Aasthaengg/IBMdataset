# あるアルファベットがN個あったとき、
# N個から一つ選ぶ or 選ばないのN + 1通り。これを全て掛け合わせ、1(一つも選ばない)を引く

import sys
readline = sys.stdin.readline

N = int(readline())
S = readline().rstrip()

from collections import defaultdict
dic = defaultdict(int)

for c in S:
  dic[c] += 1

ans = 1
DIV = 10 ** 9 + 7
for val in dic.values():
  ans *= ((val + 1) % DIV) 
  ans %= DIV
print(ans - 1)