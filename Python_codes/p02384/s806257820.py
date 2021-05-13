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
    N = int(input())
    querys = [list(map(int, input().split())) for _ in range(N)]

    for query in querys:
        dice = Dice(L)

        for i in range(3):
            for j in range(4):
                if dice.state[1] == query[1]:
                    break
                dice.north()
                
            if dice.state[1] == query[1]:
                break

            dice.west()
            

        for i in range(4):
            if dice.state[0] == query[0]:
                break
            dice.west()

        print(dice.state[2])

