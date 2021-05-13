n = int(input())
A = [int(x) for x in input().split()]
sumA = sum(A)
res = sumA
cc = 0
for a in A:
  cc += a
  res = min(res, abs(sumA - 2 * cc))
print(res)
