N, K = list(map(int, input().split()))

while True:
    if abs(N - K) >= N:
        break
    else:
        if N >= K:
            N = N - (N // K) * K
        else:
            N = N - (N // (2 * N - K)) * (2 * N - K)

print(N)