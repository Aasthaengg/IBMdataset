N, M = map(int, input().split())
S = input()
T = input()
from fractions import gcd

g = gcd(N, M)
flag = True
for k in range(g):
  if S[k * N // g] != T[k * M // g]:
    flag = False

if flag:
  print(N * M // g)
else:
  print(-1)