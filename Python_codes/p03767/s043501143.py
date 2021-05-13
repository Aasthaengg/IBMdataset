N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
k = 0
for i in range(1, len(A)-N, 2):
  k += A[i]
print(k)