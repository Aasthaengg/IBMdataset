def create_divisors(n):
  divisors=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      divisors.append(i)
      if i!=n//i:
        divisors.append(n//i)
  divisors.sort(reverse=True)
  return divisors

from math import floor
n,m=map(int,input().split())
n_max=floor(m/n)
d=create_divisors(m)
for di in d:
  if di<=n_max:
    print(di)
    exit(0)