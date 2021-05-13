N, K = map(int, input().split())
ans = min(abs(N%K), abs(N-K*(N//K+1)))
print(ans)