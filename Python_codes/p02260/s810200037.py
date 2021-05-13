N = int(raw_input())
A = map(int, raw_input().split())

counter = 0
for i in xrange(N):
  minj = i
  for j in xrange(i, N):
    if A[j] < A[minj]:
      minj = j
  if i != minj:
    tmp = A[i]
    A[i] = A[minj]
    A[minj] = tmp
    counter += 1
print " ".join(map(str, A))
print counter