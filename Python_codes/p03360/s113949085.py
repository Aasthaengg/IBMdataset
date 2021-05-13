A = list(map(int, input().split()))
A.sort(reverse=True)
K = int(input())
A[0] = A[0] * pow(2, K)

print(sum(A))