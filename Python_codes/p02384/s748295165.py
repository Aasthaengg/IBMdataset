roll_dict = dict(E = (3, 1, 0, 5, 4, 2), W = (2, 1, 5, 0, 4, 3), S = (4, 0, 2, 3, 5, 1), N = (1, 5, 2, 3, 0, 4))

dices = []
dices.append(list(map(int, input().split())))
q = int(input())

for i in "EWSN":
  dice = dices[0]
  new_dice = []
  for j in range(6):
    new_dice.append(dice[ roll_dict[i][j] ])
  dices.append(new_dice)

dice = dices[1]
new_dice = []
for i in range(6):
  new_dice.append(dice[ roll_dict["E"][i] ])
dices.append(new_dice)

for i in range(q):
  upper, front = map(int, input().split())
  for j in range(6):
    if dices[j][0] == upper:
      if dices[j][1] == front:
        print(dices[j][2])
      elif dices[j][2] == front:
        print(dices[j][4])
      elif dices[j][4] == front:
        print(dices[j][3])
      elif dices[j][3] == front:
        print(dices[j][1])

