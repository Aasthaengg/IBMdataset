import math
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
N,M=map(int,input().split())
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
if N==1:
  print(M)
else:
  ans=0
  a=M//N
  v=make_divisors(M)
  for i in range(a,0,-1):
    if M%i==0:
      print(i)
      break