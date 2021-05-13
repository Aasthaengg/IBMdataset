N, K = map(int, input().split())
A = sorted([int(input()) for i in range(N)])
B = [A[i-1]-A[i-K] for i in range(K, N+1)]
print(min(B))
