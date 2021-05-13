from itertools import product

n = int(input())
A = list(map(int, input().split()))

count = 0
for C in product((-1, 0, 1), repeat=n):
  total = 1
  for a, c in zip(A, C):
    total *= (a + c)
  if total % 2 == 0:
    count += 1
print(count)