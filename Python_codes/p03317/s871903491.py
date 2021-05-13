N, K = map(int, input().split())
ans = 1 + ((N - K) + (K - 2)) // (K - 1)
print(ans)
