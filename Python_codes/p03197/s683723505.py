N = int(input())
A = [ int(input()) for _ in range(N) ]
B = [ a % 2 for a in A ]
if sum(B) == 0:
  print("second")
else:
  print("first")