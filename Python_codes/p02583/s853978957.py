from itertools import combinations

data1 = input()
data2 = [int(i) for i in input().split(" ")]

count = 0
if len(data2) >= 3:
  for d1, d2, d3 in combinations(data2, 3):
    if d1 == d2 or d2 == d3 or d1 == d3:
      continue
    if d1 + d2 <= d3 or d1 + d3 <= d2 or d2 + d3 <= d1:
      continue
    count += 1

  print(count)
else:
  print(0)