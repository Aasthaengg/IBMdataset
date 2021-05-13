class Dice():
    
    state = [0 for _ in range(6)]

    def __init__(self, dice_list):
        self.state[0] = dice_list[0]
        self.state[1] = dice_list[1]
        self.state[2] = dice_list[2]
        self.state[3] = dice_list[3]
        self.state[4] = dice_list[4]
        self.state[5] = dice_list[5]

    def north(self):
        tmp = self.state[0]
        self.state[0] = self.state[1]
        self.state[1] = self.state[5]
        self.state[5] = self.state[4]
        self.state[4] = tmp

    def west(self):
        tmp = self.state[0]
        self.state[0] = self.state[2]
        self.state[2] = self.state[5]
        self.state[5] = self.state[3]
        self.state[3] = tmp

    def south(self):
        tmp = self.state[0]
        self.state[0] = self.state[4]
        self.state[4] = self.state[5]
        self.state[5] = self.state[1]
        self.state[1] = tmp


    def east(self):
        tmp = self.state[0]
        self.state[0] = self.state[3]
        self.state[3] = self.state[5]
        self.state[5] = self.state[2]
        self.state[2] = tmp

    
if __name__ == '__main__':
    L = list(map(int, input().split()))
    actions = list(input())

    dice = Dice(L)

    for action in actions:
        if action == 'N':
            dice.north()

        if action == 'W':
            dice.west()

        if action == 'S':
            dice.south()

        if action == 'E':
            dice.east()

    print(dice.state[0])
