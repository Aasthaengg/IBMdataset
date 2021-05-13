S = int(input())

mod = 10 ** 9 + 7

DP = [0] * (S + 11)
DP[0], DP[1], DP[2], DP[3] = 1, 0, 0, 1

C = 2
for i in range(4, S + 1):
  DP[i] = (C - DP[i - 1] - DP[i - 2]) % mod
  C = (C + DP[i]) % mod
  
print(DP[S])