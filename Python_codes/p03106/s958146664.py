def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)
def make_divisors(n):
  lower_divisors , upper_divisors = [], []
  i = 1
  while i*i <= n:
    if n % i == 0:
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]
A,B,K=map(int,input().split())
c=gcd(A,B)
print(make_divisors(c)[-K])