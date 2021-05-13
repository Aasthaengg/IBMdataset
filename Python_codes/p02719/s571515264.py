N, K = list(map(int, input().split()))
A = abs(N - (K*(N//K+1)))
B = abs(N - (K*(N//K)))
print(min(A, B))
