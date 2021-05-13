N, K = map(int, input().split())
H = []
for _ in range(N):
    H.append(int(input()))
H.sort()
res = float("inf")
for i in range(N-K+1):
    res = min(H[i+K-1]-H[i],res)
print(res)