N, K = map(int, input().split())
H = list(map(int, input().split()))

INF = 10**10
lis = [INF]*N
lis[0] = 0
for i in range(1, N):
    H_i = H[i]
    for j in range(max(0, i-K), i):
        lis[i] = min(lis[j] + abs(H[j] - H_i), lis[i])
print(lis[N-1])