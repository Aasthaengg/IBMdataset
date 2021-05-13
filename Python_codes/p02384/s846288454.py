class Dice():
    def __init__(self,num):
        self.num = num
    def n_roll(self):
        self.num = [self.num[1],self.num[5],self.num[2],self.num[3],self.num[0],self.num[4]]
    def e_roll(self):
        self.num = [self.num[2],self.num[1],self.num[5],self.num[0],self.num[4],self.num[3]]
    def r_spin(self):
        self.num = [self.num[0],self.num[2],self.num[4],self.num[1],self.num[3],self.num[5]]
dice = Dice(input().split())
n = int(input())
for i in range(n):
    top, front = input().split()
    right = ""
    if top == dice.num[0] or top == dice.num[1] or top == dice.num[4] or top == dice.num[5]:
        for j in range(4):
            if top == dice.num[0]:
                break
            dice.n_roll()
    else:
        for j in range(4):
            dice.e_roll()
            if top == dice.num[0]:
                break
    for j in range(4):
        if top == dice.num[0] and front == dice.num[1]:
            break
        dice.r_spin()
    print(dice.num[2])
