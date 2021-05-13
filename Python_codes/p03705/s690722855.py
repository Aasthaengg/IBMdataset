N,A,B = map(int, input().split())

if (A < B and N > 1) or (A==B):
  minimum_sum = A*(N-1) + B
  maximum_sum = A + B*(N-1)
  print(maximum_sum - minimum_sum + 1)
else:
  print(0)