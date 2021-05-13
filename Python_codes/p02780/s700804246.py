N, K = map(int, input().split())
p = [int(x) for x in input().split()]

ksum = [0 for _ in range(N-K+1)]
ksum[0] = sum(p[:K])
for i in range(N-K):
    ksum[i+1] = ksum[i] - p[i] + p[i+K]

print((K+max(ksum))/2)