N = int(input())
A = input()
A = [x for x in A]
B = input()
B = [x for x in B]
C = input()
C = [x for x in C]

total = 0

for i in range(N):
  if(A[i]==B[i] and A[i]!=C[i]):
      total = total+1
  if(A[i]==C[i] and A[i]!=B[i]):
      total =  total + 1
  if(B[i]==C[i] and A[i]!=B[i]):
      total = total + 1
  if(A[i]==B[i] and A[i]==C[i]):
      total = total
  if(A[i]!=B[i] and A[i]!=C[i] and B[i]!=C[i]):
      total = total + 2

print(total)
