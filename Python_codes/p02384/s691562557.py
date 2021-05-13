dice = input().rstrip().split(' ')
indication = "EEENEEENEEESEEESEEENEEENSWWSWWWNWWWNWWWSWWWSWWW"
indic = list(indication)
length = len(indic)
num = int(input())
for j in range(num):
  s = input().rstrip().split(' ')
  top = int(s[0])
  front = int(s[1])
  for i in range(length):
    newdice = [0] * 6
    if str(indic[i]) == "N":
      newdice[0] = dice[1]
      newdice[1] = dice[5]
      newdice[2] = dice[2]
      newdice[3] = dice[3]
      newdice[4] = dice[0]
      newdice[5] = dice[4]
      dice = newdice
      if int(dice[0]) == top and int(dice[1]) == front:
        print(int(dice[2]))
        break;
    elif str(indic[i]) == "S":
      newdice[0] = dice[4]
      newdice[1] = dice[0]
      newdice[2] = dice[2]
      newdice[3] = dice[3]
      newdice[4] = dice[5]
      newdice[5] = dice[1]
      dice = newdice
      if int(dice[0]) == top and int(dice[1]) == front:
        print(int(dice[2]))
        break;
    elif str(indic[i]) == "E":
      newdice[0] = dice[3]
      newdice[1] = dice[1]
      newdice[2] = dice[0]
      newdice[3] = dice[5]
      newdice[4] = dice[4]
      newdice[5] = dice[2]
      dice = newdice
      if int(dice[0]) == top and int(dice[1]) == front:
        print(int(dice[2]))
        break;
    elif str(indic[i]) == "W":
      newdice[0] = dice[2]
      newdice[1] = dice[1]
      newdice[2] = dice[5]
      newdice[3] = dice[0]
      newdice[4] = dice[4]
      newdice[5] = dice[3]
      dice = newdice
      if int(dice[0]) == top and int(dice[1]) == front:
        print(int(dice[2]))
        break;

