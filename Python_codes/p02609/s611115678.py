# -*- coding: utf-8 -*-
N = int(input())
X = input()
X_10 = int(X, 2)
popcount_X = X.count("1")
popcount_X_plus = popcount_X + 1
popcount_X_minus = popcount_X - 1
f_plus = X_10 % popcount_X_plus
f_minus = X_10 % popcount_X_minus if popcount_X_minus != 0 else 0

def popcount(n):
  return bin(n).count("1")

def f(n):
  if n == 0:
    return 0
  return n % popcount(n)

for i in range(N):
  j = N - (i + 1)
  n = 0
  ans = 1
  
  if X[i] == '0':
#    n = (f_plus + (2**j % popcount_X_plus)) % popcount_X_plus
    n = (f_plus + pow(2, j, popcount_X_plus)) % popcount_X_plus
  else:
    if popcount_X_minus == 0:
      print(0)
      continue
    else:
#      n = (f_minus - (2**j % popcount_X_minus) + popcount_X_minus) % popcount_X_minus
      n = (f_minus - pow(2, j, popcount_X_minus) + popcount_X_minus) % popcount_X_minus
  
  while n > 0:
    n = f(n)
    ans += 1
  print(ans)