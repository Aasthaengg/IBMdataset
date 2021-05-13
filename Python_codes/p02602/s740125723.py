N , K = list(map(int, input().split()))
A = list(map(int, input().split()))
score = 1
for i in range(K, N):
  if(A[i] > A[i - K]): print("Yes")
  else: print("No")
