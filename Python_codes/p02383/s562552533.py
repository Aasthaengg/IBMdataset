dice = map(int, raw_input().split())
inst = raw_input()

for i in range(len(inst)):
    if inst[i] == 'E':
        temp = dice[5]
        dice[5] = dice[2]
        dice[2] = dice[0]
        dice[0] = dice[3]
        dice[3] = temp
    elif inst[i] == 'W':
        temp = dice[5]
        dice[5] = dice[3]
        dice[3] = dice[0]
        dice[0] = dice[2]
        dice[2] = temp
    elif inst[i] == 'N':
        temp = dice[5]
        dice[5] = dice[4]
        dice[4] = dice[0]
        dice[0] = dice[1]
        dice[1] = temp
    elif inst[i] == 'S':
        temp = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[0]
        dice[0] = dice[4]
        dice[4] = temp

print dice[0]