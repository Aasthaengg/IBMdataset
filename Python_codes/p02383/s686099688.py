dice = input().split()
direction = list(input())
dice2 = []
for i in range(len(direction)):
    dice2 = dice
    if direction[i] == 'E':
        dice = [dice2[3],dice2[1],dice2[0],dice2[5],dice2[4],dice2[2]]
    elif direction[i] == 'N':
        dice = [dice2[1],dice2[5],dice2[2],dice2[3],dice2[0],dice2[4]]
    elif direction[i] == 'S':
        dice = [dice2[4],dice2[0],dice2[2],dice2[3],dice2[5],dice2[1]]
    else:
        dice = [dice2[2],dice2[1],dice2[5],dice2[0],dice2[4],dice2[3]]
print('{0}'.format(int(dice[0]))) 
