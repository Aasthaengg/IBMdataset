K, N = map(int, input().split())
A = list(map(int, input().split()))
A.append(K+A[0])

max_dist = max([A[i+1] - A[i] for i in range(N)])
print(K - max_dist)