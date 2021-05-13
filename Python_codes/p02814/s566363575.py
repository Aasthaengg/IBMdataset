from fractions import gcd
import math

def lcm(l):
  x = l[0]
  for i in range(1, len(l)):
    x = (x * l[i]) // gcd(x, l[i])
  return x  

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0]*N
cnt = [0]*N

for i in range(N):
  a = A[i]
  B[i] = a//2
  while a % 2 == 0:
    a /= 2
    cnt[i] += 1

cnt = set(cnt)
if len(cnt) != 1:
  print(0)
  exit()

x = lcm(B)
ans = 0

a = M//x
if a % 2:
  a += 1
print(a//2)