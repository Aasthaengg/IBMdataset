N, K = list(map(int, input().split()))

if N < K:
    print(0)
    exit(0)
print(N - K + 1)
