import sys

# A - Two Abbreviations
def get_lcm(a, b):
	import math
	return (a * b) // math.gcd(a, b)


def is_match(X, L):
  global M
  global T

  i = 0
  m = L//M * i

  while m + 1 < L:
    if m+1 in X.keys():
      if X[m+1] != T[i]:
        return False

    i += 1
    m = L//M * i

  return True


N, M = map(int, input().split())
S = input()
T = input()

if S[0] != T[0]:
  print(-1)
else:
  lcm = get_lcm(N, M)

  for i in range(1, 100):
    L = lcm * i
    X = dict()

    j = 0
    n = L//N * j

    while n + 1 < L:
      X[n+1] = S[j]

      j += 1
      n = L//N * j

    if is_match(X, L):
      print(L)
      exit()

  print(-1)