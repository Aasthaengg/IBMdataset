N = int(input())
A = list(map(int, input().split()))

maxA = max(A)
minA = min(A)
argmax = -1
argmin = -1
print(2*N - 1)

for i in range(N):
  if maxA == A[i]:
    argmax = i
  if minA == A[i]:
    argmin = i

if abs(maxA) >= abs(minA):
  for i in range(N):
    print(argmax+1, i+1)
  for i in range(N-1):
    print(i+1,i+2)

else:
  for i in range(N):
    print(argmin+1, i+1)
  for i in range(N-1):
    print(N-i,N-1-i)