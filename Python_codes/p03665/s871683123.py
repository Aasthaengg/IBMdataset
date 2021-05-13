from scipy.special import comb
n, p, *A = map(int, open(0).read().split())
o = sum(a%2 for a in A)
e = n - o

s = 0
for i in range(p, o+1, 2):
  s += comb(o, i, exact=True)
s *= pow(2, e)
print(s)