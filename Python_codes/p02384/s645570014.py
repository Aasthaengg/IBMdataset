class Dice:
    def __init__(self, dice):
        self.dice = dice
        self.rule={'N':(1,5,2,3,0,4),'S':(4,0,2,3,5,1),'E':(3,1,0,5,4,2),'W':(2,1,5,0,4,3)}
    def output(self):
        return self.dice
    def move(self, direction):
        for _ in direction:
            self.dice = [self.dice[y] for y in self.rule[_]]
        return self.dice

dice = Dice([int(x) for x in input().split()])
for _ in range(int(input())):
    tmp = [int(x) for x in input().split()]
    count = 0
    while dice.output()[0] != tmp[0]:
        if count > 4:
            while dice.output()[0] != tmp[0]: dice.move("E")
            break
        else:
            dice.move("N")
            count += 1

    while dice.output()[1] != tmp[1]: dice.move("ESW")
    print(dice.output()[2])
