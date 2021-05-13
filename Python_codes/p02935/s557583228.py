N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
for i in range(1, N):
  A[i] = (A[i-1] + A[i])/2
print(A[N-1])