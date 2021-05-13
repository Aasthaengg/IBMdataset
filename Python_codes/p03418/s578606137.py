import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
if K == 0:
    print(N ** 2)
    exit()
ans = 0
for b in range(1, N + 1):
    if b - 1 < K:
        continue
    ans += (N // b) * (b - K) + (max(N % b - K + 1, 0))
print(ans)