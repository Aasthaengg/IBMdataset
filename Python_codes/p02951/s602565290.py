bottle_1_max , bottle_1_input ,bottle_2_input = map(int,input().split())
bottle_2 = bottle_1_max -bottle_1_input - bottle_2_input
if bottle_2 >= 0:
  print(0)
else:
  print(abs(bottle_2))