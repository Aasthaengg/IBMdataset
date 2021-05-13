N = int(input())
minval = N

for a in range(1,N):
  sum = 0
  A = a
  B = N-a
  while A > 0:
    sum += A%10
    A = int(A/10)
  while B > 0:
    sum += B%10
    B = int(B/10)
  if minval > sum:
    minval = sum

print(minval)