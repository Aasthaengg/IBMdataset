from math import gcd
n = int(input())
A = list(map(int, input().split()))

f1 = True
f2 = True

c = [0] * (10**6+5)
for a in A:
  c[a] += 1
for i in range(2, 10**6+5):
  cnt = 0
  for j in range(i, 10**6+5, i):
    cnt += c[j]
  if cnt > 1:
    f1 = False


g = 0
for i in range(len(A)):
  g = gcd(g, A[i])
if g != 1:
  f2 = False

if f1:
  print("pairwise coprime")
elif f2:
  print("setwise coprime")
else:
  print("not coprime")