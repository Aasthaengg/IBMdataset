# 0が一つでもあれば、すべて正の数にできる
# そうでない場合、負の数の数が奇数の場合、負の数を一つ（最も絶対値が小さい）だけ残す

import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

ans = 0
minabs = 10 ** 9 + 1
haszero = False
minuscnt = 0
for i in range(len(A)):
  if A[i] == 0:
    haszero = True
  elif A[i] < 0:
    minuscnt += 1
  ans += abs(A[i])
  if abs(A[i]) < minabs:
    minabs = abs(A[i])
    
if haszero:
  print(ans)
elif minuscnt % 2 == 1:
  print(ans - minabs * 2)
else:
  print(ans)