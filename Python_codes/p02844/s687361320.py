N = int(input())
S = input()

DP = [[0] * 10 for _ in range(10)]
D = [0] * 10
L = [0] * 1000
for i in range(N):
  for j in range(10):
    for k in range(10):
      if DP[j][k] == 1:
        L[j * 100 + k * 10 + int(S[i])] = 1
  for j in range(10):
    if D[j] == 1:
      DP[j][int(S[i])] = 1
  D[int(S[i])] = 1

print(sum(L))