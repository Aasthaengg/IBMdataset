import sys
from itertools import combinations
n = int(input())

for i in range(1, 1000):
  if n == i*(i+1)//2:
    print("Yes")
    print(i+1)
    anslist = [[] for _ in range(i+1)]
    for j, v in enumerate(combinations([int(x) for x in range(i+1)], r=2)):
      anslist[v[0]].append(j+1)
      anslist[v[1]].append(j+1)
    for ans in anslist:
      print(len(ans), *ans)
    sys.exit()

print("No")