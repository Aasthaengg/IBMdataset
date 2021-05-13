S = int(input())
mod = 10 ** 9 + 7

DP = [0] * (S+1)

if S >= 3:
    DP[3] = 1

for i in range(4, S+1):
    DP[i] = DP[i-1] + DP[i-3]
    DP[i] %= mod

print(DP[-1])