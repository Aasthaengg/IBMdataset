N, M, K = map(int, input().split())
N, M = min(N, M), max(N, M)

if K % M == 0 or K % N == 0:
    print('Yes')
    exit()

for i in range(N + 1):
    k = K - M * i
    n = N - 2 * i
    if n <= 0 or k < 0:
        continue
    if k % n == 0:
        if 0 <= k // n <= M:
            print('Yes')
            exit()
else:
    print('No')