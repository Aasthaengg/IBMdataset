N = int(input())

from collections import defaultdict
d = defaultdict(lambda: -1)		#初期値を「-1」にする

d[0] = 2
d[1] = 1
def f(n):
  if d[n] == -1:
    a = f(n-1) + f(n-2)
    d[n] = a
  return d[n]

print(f(N))