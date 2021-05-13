X, Y = map(int, input().split())

A = [X]

i = 0

while A[i] <= Y:
  A.append(A[i] * 2)
  i += 1

print(i)