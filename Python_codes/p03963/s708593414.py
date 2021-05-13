N, K = map(int, input().split())


p = K
N -= 1
if N:
    for i in range(N):
        p = (K - 1) * p
print(p)