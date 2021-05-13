class Dice:
    def __init__(self):
        self.eye = {}
        for k, v in zip(['top', 'front', 'right', 'left', 'back', 'bottom'], input().split()):
            self.eye[k] = int(v)


    def roll(self, dir):
        self.dir = dir
        if self.dir == 'E':
            w = self.eye['top']
            self.eye['top'] = self.eye['left']
            self.eye['left'] = self.eye['bottom']
            self.eye['bottom'] = self.eye['right']
            self.eye['right'] = w
        elif self.dir == 'S':
            w = self.eye['top']
            self.eye['top'] = self.eye['back']
            self.eye['back'] = self.eye['bottom']
            self.eye['bottom'] = self.eye['front']
            self.eye['front'] = w
        elif self.dir == 'W':
            w = self.eye['top']
            self.eye['top'] = self.eye['right']
            self.eye['right'] = self.eye['bottom']
            self.eye['bottom'] = self.eye['left']
            self.eye['left'] = w
        elif self.dir == 'N':
            w = self.eye['top']
            self.eye['top'] = self.eye['front']
            self.eye['front'] = self.eye['bottom']
            self.eye['bottom'] = self.eye['back']
            self.eye['back'] = w


dice = Dice()
for dir in input():
    dice.roll(dir)
print(dice.eye['top'])

