N = [1, 5, 2, 3, 0, 4]
S = [4, 0, 2, 3, 5, 1]
E = [3, 1, 0, 5, 4, 2]
W = [2, 1, 5, 0, 4, 3]
dice = [dice for dice in input().split()]
dice_t = ["" for dice_t in range(6)]
direction = input()
for d in direction:
    if d == "N":
        for i in range(6):
            dice_t[i] = dice[N[i]]
    elif d == "S":
        for i in range(6):
            dice_t[i] = dice[S[i]]
    elif d == "E":
        for i in range(6):
            dice_t[i] = dice[E[i]]
    else:
        for i in range(6):
            dice_t[i] = dice[W[i]]
    for i in range(6):
        dice[i] = dice_t[i]

print(dice[0])