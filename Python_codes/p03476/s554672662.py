import math

def is_prime(x):
  if x <= 0 or x%1 != 0:
    return False
  elif x == 1:
    return False
  elif x == 2:
    return True
  elif x%2 == 0:
    return False
  else:
    for i in range(3, int(math.sqrt(x)//1)+1, 2):
      if x%i == 0:
        return False
    return True

S = [0] * (10**5+1)
for i in range(1, 10**5+1):
  if is_prime(i) and is_prime((i+1)/2):
    S[i] += 1
  S[i] += S[i-1]

Q = int(input())
for _ in range(Q):
  l, r = map(int, input().split())
  print(S[r] - S[l-1])