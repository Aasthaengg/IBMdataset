N, K = map(int,input().split())
n = N // K
print(min(-N + (n + 1) * K, N - n * K))