from collections import defaultdict as dd
from math import factorial
mod = 10 ** 9 + 7

def P(n, r):
  if r > n:
    return 1
  elif r == 0:
    return 1
  else:
    return(factorial(n) // factorial(n-r))
N, K = map(int, input().split())
D = dd(list)
for i in range(N-1):
  a, b = map(int, input().split())
  D[a-1].append(b-1)
  D[b-1].append(a-1)

Q = [0]
vstd = set()
ans = K
while Q:
  a = Q.pop()
  vstd.add(a)

  if a == 0:
    num = K-1
  else:
    num = K-2
  for b in D[a]:
#    print (a, D[a], b, vstd, Q, ans, end="->")
    if b not in vstd:
      if num <= 0 : ans = 0
      ans = (ans * num) % mod
#      print ("*", num, end="=")
      num -= 1
      Q.append(b)
#    print (ans)      

print (ans % mod)