import sys
import math
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int, input().split()))
ma = max(a)
p = [0]*(ma + 1)

for i in a:
  p[i] += 1

pairwise = True
for i in range(2, ma+1):
  cnt = 0
  for j in range(i, ma+1, i):
    cnt += p[j]
  if cnt > 1:
    pairwise = False
    break
    
if pairwise:
  print("pairwise coprime")
else:
  temp = a[0]
  for i in a:
    temp = math.gcd(temp, i)
  if temp == 1:
    print("setwise coprime")
  else:
    print("not coprime")