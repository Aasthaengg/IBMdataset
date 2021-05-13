import math
def firstprime(n):
  p = 2
  while(p <= math.sqrt(n)):
    if(n % p == 0):
      return p
    p += 1
  return n

N = int(input())
prime = [0] * 101
for i in range(2, N+1):
  n = i
  while(n > 1):
    p = firstprime(n)
    prime[p] += 1
    n = n // p
    
p2 = 0
p4 = 0
p14 = 0
p24 = 0
p74 = 0
for i in range(101):
  if(prime[i] >= 74):
    p74 += 1
  if(prime[i] >= 24):
    p24 += 1
  if(prime[i] >= 14):
    p14 += 1
  if(prime[i] >= 4):
    p4 += 1
  if(prime[i] >= 2):
    p2 += 1
p3_5_5 = p4*(p4-1)*(p2-2)//2
p5_15 = p14*(p4-1)
p3_25 = p24*(p2-1)
p75 = p74
print(p3_5_5+p5_15+p3_25+p75)