import math
A, B = map(int, input().split())

def gcd(A, B):
  if A < B:
    A, B = B, A
  while B > 0:
    temp = A % B
    A = B
    B = temp
  return A

gcd_num = gcd(A, B)

def prime(a):
  max_a = 1 + int(math.sqrt(a))
  d = dict()
  d[1] = 1
  i = 2
  while a != 1:
    if i > max_a:
      d[a] = 1
      break
    if a % i == 0:
      a = a // i
      if i in d:
        d[i] += 1
      else:
        d[i] = 1
    else:
      i += 1
  return d
d = prime(gcd_num) 

print(len(d))