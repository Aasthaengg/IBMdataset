A, B, K = input().split(' ')
A = int(A)
B = int(B)
K = int(K)
N = []
if B-A>K:
  for i in range(A, A+K):
    print(i)
    N.append(i)
  for i in range(B-K+1, B+1):
    if not i in N:
      print(i)

else:
  for i in range(A, B+1):
    if i < A + K:
      print(i)
    elif i > B-K:
      print(i)