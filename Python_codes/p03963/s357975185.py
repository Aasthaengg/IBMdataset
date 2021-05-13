N, K = map(int,input().split())
ans = min(K * (K - 1) ** (N - 1), 2 ** 31 - 1)
print(ans)