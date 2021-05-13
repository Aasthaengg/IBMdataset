N , X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = [0] + A
for i in range(N):
  A[i+1] = A[i]+A[i+1]
  if A[i+1]>X:
    break
if i==N-1 and X==A[N]:
  print(N)
else:
  print(i)
