N = int(input())
A = [0]

for s in input():
  if s=="I":
    A.append(A[-1]+1)
  else:
    A.append(A[-1]-1)

print(max(A))