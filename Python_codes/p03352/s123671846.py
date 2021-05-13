#素因数分解して列挙する関数、約数列挙ではない！
from collections import Counter
def factorize(n):
  b = 2
  fct = []
  while b * b <= n:
    while n % b == 0:
      n //= b
      fct.append(b)
    b = b + 1
  if n > 1:
    fct.append(n)
  f = Counter(fct).values()
  if 1 not in f and len(set(f))==1:
    return True
  return False

X = int(input())
for i in range(X,0,-1):
  f = factorize(i)
  if f==True or i==1:
    print(i)
    break