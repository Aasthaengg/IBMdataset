## C - Christmas Eve
N, K = map(int, input().split())
H = sorted([int(input()) for i in range(N)])
rt = 10**9
for i in range(0,N-K+1):
    rt = H[K - 1 + i] - H[i] if rt > H[K - 1 + i] - H[i] else rt
print(rt)