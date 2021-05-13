N,A,B = map(int, input().split())
if B < A:
  print(0)
else:
  print(max(0, 1+(N-2)*(B-A)))