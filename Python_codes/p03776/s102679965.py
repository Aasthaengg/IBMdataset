from operator import mul
from functools import reduce
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
N, A, B = map(int, input().split())
v = [int(c) for c in input().split()]
v.sort(reverse=True)
m = 0
for i in range(A):
  m += v[i]
ans1 = m/A
ls = []
for j in range(A,B):
  m += v[j]
  if ans1!=m/(j+1):
    break
  ls += [j]
T = v[:A]
t = set(T)
dic1 = {}
dic2 = {}
for c in t:
  dic1[c] = T.count(c)
  dic2[c] = v.count(c)
ans2 = 1
for c in t:
  ans2 *= cmb(dic2[c],dic1[c])
for l in ls:
  dic1[v[l]] += 1
  ans2 += cmb(dic2[c],dic1[c])
print(ans1)
print(ans2)