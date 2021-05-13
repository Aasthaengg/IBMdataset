n = int(input())

primes = [0]*(n+1)

def factorize(n):
  
  global primes
  arr = []
  temp = n

  for i in range(2, int(n**(1/2))+1):
    if temp % i == 0:
      while temp % i == 0:
        temp //= i
        primes[i] += 1

  if temp != 1:
    primes[temp] += 1

for i in range(2, n+1):
  factorize(i)
  
MOD = 1000000007

def mod(n):         
  return n % MOD

def multiply(a, b): #mod(a*b)を求める
  return mod(mod(a)*mod(b))

ans = 1
for i in range(n+1):
  if primes[i] > 0:
    ans = multiply(ans, primes[i]+1)
    
print(mod(ans))