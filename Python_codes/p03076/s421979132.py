from itertools import permutations

a, b, c, d, e = [int(input()) for _ in range(5)]

result = 10 ** 9

p = permutations([a, b, c, d, e])
for case in p:
  t = 0
  for i, dish in enumerate(case):
    if i != 4 and dish % 10 != 0:
      dish += 10 - dish % 10
    t += dish
  
  result = min(result, t)
  
print(result)