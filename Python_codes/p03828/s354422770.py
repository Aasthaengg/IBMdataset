import math

def is_prime(n):
  if n & 0: return False
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True
  
def prime(n):
  if n < 2: return []
  P = [2]
  for i in range(3, n+1):
    if is_prime(i):
      P.append(i)
  return P

n = int(input())
P = prime(n)
cnt = [0]*len(P)

for i in range(2, n+1):
  x = i
  pi = 0
  while x > 1 and pi < len(P):
    if x % P[pi] == 0:
      cnt[pi] += 1
      x //= P[pi]
    else:
      pi += 1

ans = 1
for c in cnt:
  ans *= c+1
  ans %= 10**9 + 7
print(ans)