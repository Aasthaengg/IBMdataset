from scipy.special import comb
n, p, *A = map(int, open(0).read().split())
odd = sum(a%2 for a in A)
even = n - odd

if p:
  s = 0
  for i in range(1, odd+1, 2):
    s += comb(odd, i, exact=True)
  s *= pow(2, even)
  print(s)
else:
  s = 0
  for i in range(0, odd+1, 2):
    s += comb(odd, i, exact=True)
  s *= pow(2, even)
  print(s)