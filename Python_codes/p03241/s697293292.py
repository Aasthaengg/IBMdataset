N, M = map(int ,input().split())

i = 1
A = []
B = []

while i*i <= M:
  if M % i == 0:
    A.append(i)
    B.append(M//i)
  i += 1 
    
for i in range(len(B)):
  if A[i] >= N:
    print(B[i])
    exit()
    
for i in range(len(A)-1,-1,-1):
  if B[i] >= N:
    print(A[i])
    exit()