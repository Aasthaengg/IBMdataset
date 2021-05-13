N, K = map(int, input().split())
H = []
for _ in range(N):
    H.append(int(input()))
H = list(sorted(H))
r_min = 10 ** 10
for i in range(N-K+1):
    n_min = H[i]
    n_max = H[i+K-1]
    r_min = min(r_min, n_max-n_min)
print(r_min)
