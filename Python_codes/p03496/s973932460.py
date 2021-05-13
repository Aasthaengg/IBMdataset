N = int(input())
A = list(map(int, input().split()))

M = max(A)
m = min(A)
print(2*N-2)

if M+m >= 0:
  a = A.index(M)
  for i in range(N):
    if i != a:
      #A[i] += M
      print(a+1, i+1)
  for i in range(N-1):
    #A[i+1] += A[i]
    print(i+1, i+2)
else:
  a = A.index(m)
  for i in range(N):
    if i != a:
      print(a+1, i+1)
  for i in range(N, 1, -1):
    print(i, i-1)