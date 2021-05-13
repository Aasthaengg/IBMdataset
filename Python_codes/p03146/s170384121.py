S = int(input())
A = [S]
if (A[0]%2) == 0:
  A.append(int(A[0]/2))
else:
  A.append(int(3*A[0]+1))
i = 1
while i >0:
  if A[i]%2 == 0:
    X = int(A[i]/2)
    if X in A:
      A.append(X)
      break
    else:
      A.append(X)
    i += 1
  else:
    X = int(3*A[i]+1)
    if X in A:
      A.append(X)
      break
    else:
      A.append(X)
    i += 1
print(len(A))