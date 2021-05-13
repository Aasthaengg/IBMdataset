class Dice:
    def __init__(self, face_vals):
        self.faces = dict(zip(['top', 'south', 'east',
                               'west', 'north', 'bottom'], face_vals))

    def roll(self, direction):
        if direction == 'N':
            self.faces['top'], self.faces['south'], self.faces['bottom'], \
            self.faces['north'] = self.faces['south'], self.faces['bottom'], \
            self.faces['north'], self.faces['top']
        elif direction == 'S':
            self.faces['top'], self.faces['south'], self.faces['bottom'], \
            self.faces['north'] = self.faces['north'], self.faces['top'], \
            self.faces['south'], self.faces['bottom']
        elif direction == 'E':
            self.faces['top'], self.faces['east'], self.faces['bottom'], \
            self.faces['west'] = self.faces['west'], self.faces['top'], \
            self.faces['east'], self.faces['bottom']
        else:
            self.faces['top'], self.faces['east'], self.faces['bottom'], \
            self.faces['west'] = self.faces['east'], self.faces['bottom'], \
            self.faces['west'], self.faces['top']


face_vals = input().split()

dice = Dice(face_vals)

for i in input():
    dice.roll(i)

print(dice.faces['top'])