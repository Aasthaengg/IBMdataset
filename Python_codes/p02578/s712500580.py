N = int(input())
A = [int(s) for s in input().split()]
ma = A[0]
total = 0
for a in A:
  if a < ma:
    total += ma - a
  ma = max(ma, a)
print(total)
