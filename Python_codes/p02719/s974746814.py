N, K = list(map(int, input().split()))
a = N // K
b = N % K
print(min(abs(N - K * a), abs(b - K)))