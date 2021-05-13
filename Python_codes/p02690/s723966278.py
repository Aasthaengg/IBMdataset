
x = int(input())
y = int(pow(x, 1/5))*2
A = [i**5 for i in range(y+1)]
B = [i**5 for i in range(y+1)]

for i in range(len(A)):
  for j in range(len(B)):
    if ( A[i] + B[j] ) == x:
      if A[i] > B[j]:
        exit(print(i, -j))
      else:
        exit(print(j, -i))
    elif ( A[i] - B[j] ) == x:
      exit(print(i, j))
