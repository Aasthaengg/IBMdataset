import sys
from math import gcd
input = sys.stdin.readline
N, M = map(int, input().split())
S = list(input())[: -1]
T = list(input())[: -1]
g = gcd(N, M)
ln = N * M // g
x = 0
y = 0
while x < N and (y < M):
  if S[x] != T[y]:
    print(-1)
    exit(0)
  x += ln // M
  y += ln // N
print(ln)