N, K = map(int, input().split())
ans = K * pow(K - 1, N - 1)
print(ans)
