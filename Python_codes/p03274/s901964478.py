N, K = map(int,input().split())
C = list(map(int,input().split()))

K -= 1
D = 10**9
for i in range(N-K):
    d = C[i+K] - C[i]
    L = d + abs(0 - C[i])
    R = d + abs(0 - C[i+K])
    D = min(D,min(L,R))

print(D)
