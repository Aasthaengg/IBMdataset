class Dice:
    def __init__(self, labels):
        self.labels = labels
    def east(self):
        self.labels[0], self.labels[2], self.labels[5], self.labels[3] = self.labels[3], self.labels[0], self.labels[2], self.labels[5]
    def west(self):
        self.labels[0], self.labels[2], self.labels[5], self.labels[3] = self.labels[2], self.labels[5], self.labels[3], self.labels[0]
    def north(self):
        self.labels[0], self.labels[1], self.labels[5], self.labels[4] = self.labels[1], self.labels[5], self.labels[4], self.labels[0]
    def south(self):
        self.labels[0], self.labels[1], self.labels[5], self.labels[4] = self.labels[4], self.labels[0], self.labels[1], self.labels[5]

dice = Dice(list(map(int, input().split())))

for n in range(int(input())):
    top, foward = map(int, input().split())
    south_cnt = 0

    while True:
        #print(dice.labels[0], dice.labels[1], dice.labels[2], dice.labels[4], dice.labels[3])
        if foward == dice.labels[1] and top == dice.labels[0]:
            break
        if foward == dice.labels[1]:
            dice.east()
        elif top == dice.labels[0]:
            dice.south()
            dice.east()
            dice.north()
        else:
            if south_cnt == 3:
                dice.east()
            else:
                dice.south()
                south_cnt += 1
    print(dice.labels[2])


