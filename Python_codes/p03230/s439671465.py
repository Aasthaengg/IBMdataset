n=int(input())
if int((2*n)**(1/2))*int((2*n)**(1/2)+1)==2*n:
  a=int((2*n)**(1/2))
  print("Yes")
  print(a+1)
  A=[[] for i in range(a+1)]
  x=0
  for i in range(a):
    for j in range(a-i):
      x=x+1
      A[i].append(x)
  B=[[] for i in range(a+1)]
  x=0
  for i in range(a):
    for j in range(a-i):
      x=x+1
      B[i].append(x)
  C=[[] for i in range(a+1)]
  for i in range(a):
    for j in range(a-i):
      C[a-j].append(B[i][j])
  D=[[] for i in range(a+1)]
  for i in range(a+1):
    D[i]=A[i]+C[i]
  for i in range(a+1):
    print(a,end=" ")
    for j in range(a):
      print(D[i][j],end=" ")
    print()
else:
  print("No")