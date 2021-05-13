def open(box, key):
    return (box & (2**N-1 - key))
N, M = map(int, input().split())
INF = 10**8+1
dp = [[INF]*2**N for i in range(M+1)]
for i in range(M+1):
    dp[i][0] = 0
key = []
for i in range(M):
    a, b= map(int, input().split())
    n = 0
    c = list(map(int, input().split()))
    for i in range(b):
        n += 2**(c[i]-1)
    key.append((a,n))
for i in range(1,M+1):
    for j in range(2**N):
        dp[i][j] = min(dp[i-1][j], dp[i-1][open(j, key[i-1][1])]+key[i-1][0])
if dp[M-1][2**N-1] == INF:
    dp[M-1][2**N-1] = -1
print(dp[M-1][2**N-1])