[K, N] = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))

max_distance = K - A[-1] + A[0]
for i in range(len(A)-1):
    max_distance = max(max_distance, A[i+1] - A[i])

print(K - max_distance)


