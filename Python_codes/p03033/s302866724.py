import sys
from bisect import bisect_left
input = sys.stdin.readline

N,Q = map(int, input().split())
STX = [list(map(int, input().split())) for _ in range(N)]
D = [int(input()) for _ in range(Q)]

STX = sorted(STX, key=lambda x: x[2])

MASK = [-1]*Q
ANS = [-1]*Q

for (s,t,x) in STX:
  s2 = (s - x)
  t2 = (t - x)

  start = bisect_left(D, s2)
  end = bisect_left(D, t2, lo=start)

  #print(start, end, DI)
  while (start < end):
    if (-1 == MASK[start]):
      ANS[start] = x
      MASK[start] = end
      start += 1
    else:
      start = MASK[start]


print(*ANS, sep='\n')
