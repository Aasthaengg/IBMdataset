from functools import reduce
_, k, *lst = map(int, open(0).read().split())
def gcd(a, b):
  while b:
    a, b = b, a%b
  return a
a = reduce(gcd, lst)
print('IMPOSSIBLE' if k > max(lst) or k % a else 'POSSIBLE')
