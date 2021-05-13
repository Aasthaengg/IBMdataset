import math
N = int(input())
ans = int((-1+math.sqrt(1+8*N))/2)

if (ans*(ans+1))//2<N:
  ans += 1

k = (ans*(ans+1))//2-N

if k == 0:
  for i in range(ans):
    print(i+1)
else:
  for i in range(ans):
    if i+1 != k:
      print(i+1)