from collections import defaultdict
N = int(input())
p = 10 ** 9 + 7
C = [0] * (N + 1)
D = defaultdict(lambda: -1)
DP = [[0, 0] for i in range(N + 1)]
DP[0] = [1, 0]
for i in range(1, N + 1):
  C[i] = int(input())
  DP[i][0] = sum(DP[i - 1]) % p
  if C[i] != C[i - 1]:
    DP[i][1] = sum(DP[D[C[i]]]) if D[C[i]] != -1 else 0
    D[C[i]] = i
print(sum(DP[N]) % p)