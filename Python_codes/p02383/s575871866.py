class Dice:
    def __init__(self,d1,d2,d3,d4,d5,d6):
        self.dice = [d1,d2,d3,d4,d5,d6]
    def turn(self,dir):
        if dir == 'S':
            self.dice = [self.dice[4],self.dice[0],self.dice[2],self.dice[3],self.dice[5],self.dice[1]]
        if dir == 'N':
            self.dice = [self.dice[1],self.dice[5],self.dice[2],self.dice[3],self.dice[0],self.dice[4]]
        if dir == 'W':
            self.dice = [self.dice[2],self.dice[1],self.dice[5],self.dice[0],self.dice[4],self.dice[3]]
        if dir == 'E':
            self.dice = [self.dice[3],self.dice[1],self.dice[0],self.dice[5],self.dice[4],self.dice[2]]

dice_num = input().split()
direction = input()

init_Dice = Dice(dice_num[0],dice_num[1],dice_num[2],dice_num[3],dice_num[4],dice_num[5])
for a in range(len(direction)):
    init_Dice.turn(direction[a])
print(init_Dice.dice[0])

