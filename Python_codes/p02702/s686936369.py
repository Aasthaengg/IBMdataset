S = list(map(int, input()))
L = len(S)
mod = 2019
T = []
A = [0 for i in range(mod)]
t = 0
p = 1
for i in range(L-1, -1, -1):
  t = (t + S[i] * p) % mod
  A[t] += 1
  p = (p * 10) % mod
print(A[0] + sum([a * (a-1) // 2 for a in A]))