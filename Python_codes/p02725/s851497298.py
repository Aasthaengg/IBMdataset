K, N = map(int, input().split())
A = list(map(int, input().split()))
X = [K-A[-1]+A[0]] + [A[i]-A[i-1] for i in range(1, len(A))]
print(sum(sorted(X)[:-1]))
