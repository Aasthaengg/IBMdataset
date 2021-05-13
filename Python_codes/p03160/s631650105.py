N = int(input())
H = [0] + list(map(int, input().split()))

DP = [0]*(N+1)

for i in range(2, N+1):
    if i == 2:
        DP[i] = abs(H[1] - H[2])
        continue
    c1 = abs(H[i-1] - H[i])
    c2 = abs(H[i-2] - H[i])
    DP[i] = min(DP[i-1] + c1, DP[i-2] + c2)


print(DP[N])
