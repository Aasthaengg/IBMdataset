A = list(map(int, input().split()))
A.sort(reverse=True)
A = [A[i-1]-A[i] for i in range(1, len(A))]
print(sum(A))