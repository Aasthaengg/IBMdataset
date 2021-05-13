class Town:
  def __init__(self,x,y):
    self.x = x
    self.y = y

from itertools import permutations

N = int(input())
towns = []
for n in range(N):
  d = input().split()
  x, y = map(int, d)
  towns.append(Town(x,y))

roots = list(permutations(towns))

distances = 0
for root in roots:
  distance = 0
  for i in range(len(root) - 1 ):
    start = root[i]
    end = root[i + 1]
    distance += ((start.x - end.x) ** 2 + (start.y - end.y) ** 2) ** (1 / 2)
  distances += distance

average = distances / len(roots)
print(average)