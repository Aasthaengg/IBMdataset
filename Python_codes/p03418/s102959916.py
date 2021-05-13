import sys
input = sys.stdin.readline
N, K = [int(x) for x in input().strip().split()]

ans = 0
for m in range(1, N+1):
    if m <= K:
        continue
    maxlen, mod = divmod(N, m)
    ans += maxlen * (m - K)
    
    ans += max(0, N - m * maxlen - K + 1)
    if K == 0:
        ans -= 1
print(ans)