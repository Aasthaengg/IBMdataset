A = input()
B = input()
finished = False
 
if len(A) > len(B):
  print("GREATER")
  finished = True
elif len(A) < len(B):
  print("LESS")
  finished = True
else:
  for i in range(len(A)):
    if A[i] > B[i]:
      print("GREATER")
      finished = True
      break
    elif A[i] < B[i]:
      print("LESS")
      finished = True
      break
 
if not finished:
  print("EQUAL")
