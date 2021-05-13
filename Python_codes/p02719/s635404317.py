N, K = list(map(int, input().split()))
surplus = N % K
ans = min(surplus, K - surplus)
print(ans)