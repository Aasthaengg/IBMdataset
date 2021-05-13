N, M = (int(i) for i in input().split())
cos = [0] * M
bit = [0] * M
for i in range(M):
    a, b = (int(j) for j in input().split())
    cos[i] = a
    c = [int(j) for j in input().split()]
    bit[i] = sum([2 ** (j-1) for j in c])

DP = [[float("inf")] * 2**N for counter1 in range(M+1)]
for i in range(M):
    DP[i][0] = 0

for i in range(M):
    a = cos[i]
    bi = bit[i]
    for j in range(2**N):
        DP[i+1][j|bi] = min(DP[i+1][j|bi], DP[i][j] + a)
        DP[i+1][j] = min(DP[i+1][j], DP[i][j])

ans = DP[M][2**N-1]
if ans == float("inf"):
    print(-1)
else:
    print(ans)