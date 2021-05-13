# ある文字を起点としたとき、ある文字同士に挟まれた区間の最大値が操作回数
# jackal -> aに挟まれた最大区間は2
# 100文字で、アルファベット26種類なので全通り試す

import sys
readline = sys.stdin.readline

S = readline().rstrip()

a = ord("a")
z = ord("z")

ans = 10 ** 10
for i in range(a,z + 1):
  arr = S.split(chr(i))
  maxlen = 0
  for a in arr:
    if len(a) > maxlen:
      maxlen = len(a)
  if maxlen < ans:
    ans = maxlen
  
print(ans)