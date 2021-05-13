# 一度に食べられるリンゴを一つの山だと考える
# 青　青　青
# 赤　赤
# 黄
# だとすると、
# 青赤黄
# 青赤
# 青
# の3つの山があると考えてよい
# この山を想定したときに、各山のXORが0であればsecond、そうでなければfirst

N=int(input())
A=[0] * N
for i in range(N):
  A[i] = int(input())
  
A = sorted(A)
minus = 0
m = []
for i in range(len(A)):
  if (A[i] - minus)%2 == 1:
    m += [N-i]
  minus = A[i] + minus

if len(m) == 0:
  print("second")
else:
  from functools import reduce
  r = reduce(lambda x,y:x^y,m)
  print(("first","second")[r == 0])