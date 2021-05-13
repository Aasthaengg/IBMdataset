N, K = map(int, input().split())
H = list(map(int, input().split()))

INF = 10**9 + 1
L = [INF]*N
L[0] = 0
for i in range(1, N):
    minLi = L[i]
    H_i = H[i]
    for k in range(1, K+1):
        if i - k >= 0:
            minLi = min(minLi, L[i-k] + abs(H_i - H[i-k]))
    L[i] = minLi
print(L[N-1])
