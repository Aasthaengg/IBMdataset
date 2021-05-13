class Dice:
    def __init__(self, face_vals):
        self.faces = dict(zip(['top', 'front', 'right',
                               'left', 'back', 'bottom'], face_vals))

    def roll(self, direction):
        if direction == 'N':
            self.faces['top'], self.faces['front'], self.faces['bottom'], \
            self.faces['back'] = self.faces['front'], self.faces['bottom'], \
            self.faces['back'], self.faces['top']
        elif direction == 'S':
            self.faces['top'], self.faces['front'], self.faces['bottom'], \
            self.faces['back'] = self.faces['back'], self.faces['top'], \
            self.faces['front'], self.faces['bottom']
        elif direction == 'E':
            self.faces['top'], self.faces['right'], self.faces['bottom'], \
            self.faces['left'] = self.faces['left'], self.faces['top'], \
            self.faces['right'], self.faces['bottom']
        else:
            self.faces['top'], self.faces['right'], self.faces['bottom'], \
            self.faces['left'] = self.faces['right'], self.faces['bottom'], \
            self.faces['left'], self.faces['top']


face_vals = input().split()

dice = Dice(face_vals)

for i in input():
    dice.roll(i)

print(dice.faces['top'])