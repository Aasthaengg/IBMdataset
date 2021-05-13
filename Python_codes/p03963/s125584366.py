N, K = [int(_) for _ in input().split()]

ret = K
for i in range(N-1):
    ret *= (K-1)

print(ret)
