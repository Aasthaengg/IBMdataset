import sys

# A - Multiple Array
N = int(input())
A, B =[], []

for _ in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

A.reverse()
B.reverse()
count = 0

for i in range(N):
  a = A[i] + count

  if a % B[i] != 0:
    quotient = a // B[i]
    count += B[i] * (quotient+1) - a

print(count)