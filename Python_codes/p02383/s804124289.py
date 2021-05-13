class Dice:
    def __init__(self,num):
        self.num = num.copy()
        
    def east(self):
        temp = self.num.copy()
        self.num[1-1] = temp[4-1]
        self.num[4-1] = temp[6-1]
        self.num[6-1] = temp[3-1]
        self.num[3-1] = temp[1-1]

    def north(self):
        temp = self.num.copy()
        self.num[1-1] = temp[2-1]
        self.num[2-1] = temp[6-1]
        self.num[6-1] = temp[5-1]
        self.num[5-1] = temp[1-1]

    def south(self):
        temp = self.num.copy()
        self.num[1-1] = temp[5-1]
        self.num[5-1] = temp[6-1]
        self.num[6-1] = temp[2-1]
        self.num[2-1] = temp[1-1]

    def west(self):
        temp = self.num.copy()
        self.num[1-1] = temp[3-1]
        self.num[3-1] = temp[6-1]
        self.num[6-1] = temp[4-1]
        self.num[4-1] = temp[1-1]

num = list(map(int,input().split()))
dice = Dice(num)
command = input()
for c in command:
    if   c == 'E': dice.east()
    elif c == 'N': dice.north()
    elif c == 'S': dice.south()
    elif c == 'W': dice.west()
print(dice.num[0])
        

