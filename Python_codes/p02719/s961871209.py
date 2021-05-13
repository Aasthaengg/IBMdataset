N, K = list(map(int, input().split()))
print(min(abs(N - (K*(N//K+1))), abs(N - (K*(N//K)))))