# 148c

from sys import stdin
import fractions

#stdin = open("test/abc148_d_sample-3.in")

N = int(stdin.readline().strip())
a = list(map(int, stdin.readline().strip().split()))

rem = 0
ne = 1
ok = False

for ai in a:
  #print(ne, ai, rem)
  if ai==ne:
    ne += 1
    ok = True
  else:
    rem += 1

if ok:
  print(rem)
else:
  print("-1")
