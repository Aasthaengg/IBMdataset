N, K = map(int, input().split())
A = list(map(int, input().split()))


for i in range(len(A)-K):
  if A[i] < A[K+i]:
    print("Yes")
  else:
    print("No")