class Dice(object):
    def __init__(self):
        self.number = [0 for _ in range(6)]
        self.before = [0 for _ in range(6)]

    def set_number(self, l):
        for i in range(6):
            self.number[i] = l[i]

    def roll(self, loc):
        d = {
            'N': (1, 5, 2, 3, 0, 4),
            'S': (4, 0, 2, 3, 5, 1),
            'E': (3, 1, 0, 5, 4, 2),
            'W': (2, 1, 5, 0, 4, 3)
        }
        for i in range(6):
            self.before[i] = self.number[i]

        for i, j in enumerate(d[loc]):
            self.number[i] = self.before[j]

    def roll_clockwise(self):
        for i in range(6):
            self.before[i] = self.number[i]
        self.number = [self.before[i] for i in (0, 2, 4, 1, 3, 5)]

    def set_Top_and_Front(self, top, front):
        top_index = self.number.index(top)
        if top_index == 5:
            self.roll('E')
            self.roll('E')
        elif top_index == 4:
            self.roll('S')
        elif top_index == 3:
            self.roll('E')
        elif top_index == 2:
            self.roll('W')
        elif top_index == 1:
            self.roll('N')
        front_index = self.number.index(front)
        if front_index == 1:
            pass
        elif front_index == 2:
            self.roll_clockwise()
        elif front_index == 3:
            self.roll_clockwise()
            self.roll_clockwise()
            self.roll_clockwise()
        elif front_index == 4:
            self.roll_clockwise()
            self.roll_clockwise()

    def get_Top(self):
        return self.number[0]

    def get_right(self):
        return self.number[2]


if __name__ == '__main__':
    l = list(map(int, input().split()))
    dice = Dice()
    dice.set_number(l)
    m = int(input())
    for _ in range(m):
        i, j = list(map(int, input().split()))
        dice.set_Top_and_Front(i, j)
        print(dice.get_right())

