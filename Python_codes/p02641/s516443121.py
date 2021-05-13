import sys

X, N = map(int,input().split())
P = []
if N != 0:
  P = list(map(int,input().split()))

table = [True]*102

for i in range(N):
  table[P[i]] = False

ans = 1e18
dif = 1e18

for i in range(0,102):
  if table[i] == False:
    continue
  elif abs(i-X) > dif:
    continue
  elif abs(i-X) == dif:
    if i < ans:
      ans = i
      dif = abs(i-X)
  else:
    ans = i
    dif = abs(i-X)

print(ans)