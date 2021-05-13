from itertools import accumulate
N, X = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
p = list(accumulate(a))

result = 0
for i, x in enumerate(p):
  if X < x:
    break
  if i == N-1 and x != X:
    break
  result += 1

print(result)