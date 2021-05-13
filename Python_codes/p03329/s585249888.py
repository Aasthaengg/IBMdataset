N = int(input())

P = [1]

for i in range(1, N):
    if 6**i > N:
        break
    P.append(6**i)

for i in range(1, N):
    if 9**i > N:
        break
    P.append(9**i)

P.sort()

DP = [float('inf')] * (N + 1)
DP[0] = 0
for i in range(N):
    for p in P:
        if i + p > N:
            break
        DP[i+p] = min(DP[i+p], DP[i] + 1)
print(DP[N])
