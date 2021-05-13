N = int(input())
A = list(map(float, input().split()))

A.sort(reverse = True)

while len(A) > 1:
  x = A[-1]
  A.pop()
  y = A[-1]
  A.pop()
  A.append((x + y) / 2)
  A.sort(reverse = True)

print(A[0])