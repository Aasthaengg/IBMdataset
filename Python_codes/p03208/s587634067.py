N, K = map(int, input().split())
hs = [int(input()) for i in range(N)]
hs.sort()

m = hs[K-1] - hs[0]
for i in range(1,N-K+1):
    m = min(m, hs[i + K - 1] - hs[i])
print(m)