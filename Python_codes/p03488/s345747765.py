import numpy as np

s = input() + "T"
x, y = map(int, input().split())
A = []
B = []
now = 0
di = 1
for i in s:
  if i=="T":
    if di:
      A.append(now)
    else:
      B.append(now)
    now = 0
    di ^= 1
  else:
    now += 1

def test(L, dist):
  dist = abs(dist)
  su = sum(L)
  l = len(L)
  if su < dist or (su-dist)%2:
    return False
  can = (su-dist)//2
  dp = np.zeros(can+1, dtype=bool)
  dp[0] = True
  for i in L:
    if i <= can:
      dp[i:] |= dp[:can+1-i]
  return dp[-1]

if s[0] == "F":
  a = test(A[1:], x-A[0])
else:
  a = test(A, x)
b = test(B, y)
if a and b:
  print("Yes")
else:
  print("No")