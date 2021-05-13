K = int(input())
A = [int(_) for _ in input().split()]

A.reverse()
maximum = 2
minimum = 2
able = True

for i in range(K):
  maximum = (maximum // A[i]) * A[i] + A[i] - 1
  minimum = ((minimum - 1) // A[i] + 1) * A[i]
  if minimum > maximum:
    able = False
    break

if able:
  print(str(minimum) + ' ' + str(maximum))
else:
  print(-1)