dice = list(map(str, input().split()))
direction = input()
for i in range(len(direction)):
    if direction[i] == "N":
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif direction[i] == "S":
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif direction[i] == "W":
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
print(dice[0])