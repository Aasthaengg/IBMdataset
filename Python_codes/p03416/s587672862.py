A, B = input().split(' ')
A = int(A)
B = int(B)
count = 0
for i in range(B-A+1):
  A = str(A)
  if A == A[::-1]:
    count += 1
  A = int(A)
  A += 1
print(count)