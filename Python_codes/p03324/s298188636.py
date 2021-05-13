D, N = map(int, input().split())
skips = N // 100
print((100 ** D) * (N+skips))
