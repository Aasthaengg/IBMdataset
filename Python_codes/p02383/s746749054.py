face = map(int, raw_input().split())
order = raw_input()

dice = [ [ 0, face[0] ],
              [ 1, face[1] ],
              [ 2, face[2] ],
              [ 3, face[3] ],
              [ 4, face[4] ],
              [ 5, face[5] ]]
temp = 0

for i in order:
    if i == 'N':
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[5][1]
        dice[5][1] = dice[4][1]
        dice[4][1] = temp
    if i == 'E':
        temp = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = dice[5][1]
        dice[5][1] = dice[2][1]
        dice[2][1] = temp
    if i == 'S':
        temp = dice[0][1]
        dice[0][1] = dice[4][1]
        dice[4][1] = dice[5][1]
        dice[5][1] = dice[1][1]
        dice[1][1] = temp
    if i == 'W':
        temp = dice[0][1]
        dice[0][1] = dice[2][1]
        dice[2][1] = dice[5][1]
        dice[5][1] = dice[3][1]
        dice[3][1] = temp

print dice[0][1]