N, K = list(map(lambda n: int(n), input().split(" ")))

print(K * ((K-1) ** (N-1)))
