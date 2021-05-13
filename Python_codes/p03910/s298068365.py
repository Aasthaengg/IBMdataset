N = int(input())

import math

ans = []

def calc(N):
  ans_q = math.ceil((2*N+1/4)**(1/2)-1/2)
  ans.append(ans_q)
  return N-ans_q

while N != 0:
  N = calc(N)

[print(x) for x in sorted(ans)]