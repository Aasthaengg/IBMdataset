A = [int(input()) for i in range(3)] 
a, b = 0, 0
for j in range(min(A[0],A[1])):
  if a < A[2]:
    a += max(A[0],A[1])
    b += 1
  else:
    break
print(b)