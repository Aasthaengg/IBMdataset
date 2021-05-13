n = int(input())
A = [int(x) for x in input().split()]
res = 1
for a in A:
  if a%2 == 0:
    res *= 2
print(3 ** n - res)