import math

N = int(input())
A = list(map(int,input().split()))
MAX_INT = 10**6
f1 = [0] * (MAX_INT+1)
for a in A:
  f1[a] += 1

flg = True
for i in range(2, MAX_INT+1):
  cnt = 0
  for j in range(i, MAX_INT+1, i):
    cnt += f1[j]
  if cnt > 1:
    flg = False
    break

if flg:
  print("pairwise coprime")
  exit()

g = A[0]
for i in range(1, N):
  g = math.gcd(g, A[i])

if g == 1:
  print("setwise coprime")
else:
  print("not coprime")