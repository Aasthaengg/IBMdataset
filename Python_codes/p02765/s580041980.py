n,r = map(int, raw_input().split(' '))
def f(n,r):
  if n >= 10:
    return r
  else:
    return r + 100 * (10 - n)
print f(n,r)