N = int(input())
A = [int(s) for s in input().split()]
S = [[0] * 20 for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(20):
        S[i][j] = S[i-1][j] + (1 if A[i-1] & (1 << j) else 0)

ans = 0
i = 0
for j in range(N):
    while not all(S[j + 1][v] - S[i][v] < 2 for v in range(20)):
        i += 1
    ans += j + 1 - i
print(ans)
