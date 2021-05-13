from math import gcd
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return set(a)
  
n = int(input())
a = list(map(int, input().split()))
dic = {}
g = a[0]
flg = True
for i in range(n):
  g = gcd(g, a[i])
  if flg:
    tmp = prime_factorize(a[i])
    for j in tmp:
      if j in dic:
        flg = False
      else:
        dic[j]=1
        
if flg:
  print("pairwise coprime")
elif g == 1:
  print("setwise coprime")
else:
  print("not coprime")
