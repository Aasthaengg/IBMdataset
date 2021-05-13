N = int(input())
A = str(input())
B = str(input())
C = str(input())
count = 0
for i in range(0,N,1):
  if (A[i] != B[i] and A[i] != C[i] and B[i] != C[i]):
    count += 2
  elif (A[i] == B[i] and A[i] != C[i]) or \
       (A[i] == C[i] and A[i] != B[i]) or \
       (B[i] == C[i] and A[i] != B[i]):
    count += 1
print(count)