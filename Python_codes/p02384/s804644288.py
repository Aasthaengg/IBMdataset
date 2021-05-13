def rotate(dice,d):
    if d == "N":
        temp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp
    elif d == "E":
        temp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp
    elif d == "W":
        temp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp
    elif d == "S":
        temp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
    elif d == "R":
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[4]
        dice[4] = dice[3]
        dice[3] = temp
    return dice

dice = input().split()
for j in range(int(input())):
    t,f = map(str, input().split())
    flag = False
    i = 0
    while True:
        if dice[0] == t:
            while True:
                if dice[1] == f:
                    print(dice[2])
                    flag = True
                    break
                else:
                    dice = rotate(dice, "R")
        if flag:
            break
        if i%2 == 0:
            dice = rotate(dice, "N")
        else:
            dice = rotate(dice, "E")
        i += 1