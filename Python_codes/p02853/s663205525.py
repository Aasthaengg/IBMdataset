from collections import defaultdict

x, y = [int(i) for i in input().split()]
prize = defaultdict(int)
prize[1] = 300000
prize[2] = 200000
prize[3] = 100000

if x == 1 and y == 1:
  print(prize[1] + prize[1] + 400000)
  exit(0)

print(prize[x] + prize[y])