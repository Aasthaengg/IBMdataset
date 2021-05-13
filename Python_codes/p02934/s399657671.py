N = int(input())
A  = list(map(int, input().split()))
for i in range(len(A)):
  A[i] = 1/A[i]
print(1/sum(A))