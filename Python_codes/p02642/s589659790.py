from collections import Counter

N = int(input())
A = [int(Ai) for Ai in input().split()]

counter = Counter(A)

dp = [1] * (max(A) + 1)
for Ai in A:
    for j in range(Ai * 2, len(dp), Ai):
        dp[j] = 0

print(sum([dp[Ai] == 1 and counter[Ai] == 1 for Ai in A]))
