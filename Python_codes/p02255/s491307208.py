N = int(raw_input())
A = map(int, raw_input().split())
print " ".join(map(str, A))
for i in xrange(1, len(A)):
  key = A[i]
  j = i-1
  while j >= 0 and A[j] > key:
    A[j+1] = A[j]
    j -= 1
  A[j+1] = key
  print " ".join(map(str, A))