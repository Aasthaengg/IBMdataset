N = int(input())
C = [input() for i in range(N)]

MOD = 1e9 + 7

C2 = []
re = ""
L = {}
LL = [-1] * N
for i in C:
  if i != re:
    if i in L:
      LL[L[i]] = len(C2)
      L[i] = len(C2)
    else:
      L[i] = len(C2)
    C2.append(i)
  re = i


DP = [-1] * (len(C2) + 1)

DP[-1] = 1
for i in range(len(C2) - 1, -1, -1):
  DP[i] = DP[i + 1]
  if LL[i] != -1:
    DP[i] += DP[LL[i]] % MOD
print(int(DP[0] % MOD))
