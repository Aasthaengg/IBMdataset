n = int(input())
A = list(map(int, input().split()))
maxA = max(A)
abs_min = 10**9
A.remove(maxA)
for a in A:
  if abs_min > abs(maxA/2 - a):
    abs_min = abs(maxA/2 - a)
    r = a
print(maxA, r)
