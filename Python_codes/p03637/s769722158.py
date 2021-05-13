n = int(input())
a = list(map(int, input().split()))

one = 0
two = 0
four = 0
for i in a:
  if i%4 == 0: four += 1
  elif i%2 == 0: two += 1
  else: one += 1

if four-one-two%2 >= -1: print("Yes")
else: print("No")