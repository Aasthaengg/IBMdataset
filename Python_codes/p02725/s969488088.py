K, N = map(int, input().split())
A = [int(i) for i in input().split()]
distance = [abs(A[i] - A[i-1]) for i in range(1, N)]
distance.append((A[0] + (K - A[-1]))) #distance between first and last
print(sum(distance) - max(distance))