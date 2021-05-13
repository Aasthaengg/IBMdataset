from fractions import gcd
N, M = map(int, input().split())
S = input()
T = input()
g = gcd(N, M)
lcm = N * M // g
for i in range(g):
  if S[i*N//g] != T[i*M//g]:
    print(-1)
    exit()
print(lcm)