import math
answer = 0
K = int(input())
for a in range(1, K+1):
  for b in range(1, K+1):
    for c in range(1, K+1):
      answer += math.gcd(math.gcd(a, b), c)
print(answer)
