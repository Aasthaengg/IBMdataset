import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N, A, B = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse = True)
d = dd(int)
sd = dd(int)
res = 1
nCr = {}
def cmb(n, r):
  global nCr
  if r == 0 or r == n: return 1
  if r == 1: return n
  if (n,r) in nCr: return nCr[(n,r)]
  nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
  return nCr[(n,r)]

for i in range(N):
  d[v[i]] += 1
r = sum(v[: A])
s = v[: A]
sdsum = 0
for t in s:
  sd[t] += 1
  sdsum += 1
kss = sorted(sd.keys())
#print(d, sd)
f = 0
j = -1
for k in range(A, B + 1):
  j += 1
  t = 1
  for i in range(len(kss)):
    a = kss[i]
    if d[a] < sd[a] + j:
      f = 1
      break
    t *= cmb(d[a], sd[a] + j)
    #print(d[a], sd[a] + j)
  if f:
    break
  res += t
print(r / A)
print(res - 1)