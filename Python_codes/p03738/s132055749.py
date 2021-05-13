A=input()
B=input()
a=len(A)
b=len(B)
if a>b:
  print("GREATER")
elif b>a:
  print("LESS")
else:
  i=0
  while i<a:
    if A[i]>B[i]:
      print("GREATER")
      break
    elif B[i]>A[i]:
      print("LESS")
      break
    else:
      i=i+1
      if i==a:
        print("EQUAL")