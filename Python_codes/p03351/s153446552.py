A = list(map(int, input().split()))

if max(abs(A[0]-A[1]),abs(A[1]-A[2])) <= A[3] or abs(A[0]-A[2]) <= A[3]:
  print('Yes')
  exit()
print('No')
