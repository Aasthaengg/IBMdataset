from collections import defaultdict

N = int(input())
S1 = input()
S2 = input()

D = defaultdict(int)

mod = 10**9 + 7

for x in S1:
  D[x] += 1

def cnt(x, y):
  if x == 1 and y == 1:
    return 2
  elif x == 1 and y == 2:
    return 2
  elif x == 2 and y == 1:
    return 1
  else:
    return 3

L = list(D.values())
n = len(L)

ans = 1
if L[0] == 1:
  ans *= 3
else:
  ans *= 6

for i in range(1, n):
  ans *= cnt(L[i-1], L[i])
  ans %= mod

print(ans)