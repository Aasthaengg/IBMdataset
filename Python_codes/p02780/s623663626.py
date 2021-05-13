N, K = map(int, input().split())
P = list(map(int, input().split()))
ma = s = sum(P[:K])
for i in range(N-K):
    s += P[K+i] - P[i]
    ma = max(ma, s)
print((ma+K)/2)
