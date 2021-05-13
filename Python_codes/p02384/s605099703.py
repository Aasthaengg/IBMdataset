class Dice:
    def __init__(self, face_vals):
        self.faces = dict(zip(['top', 'front', 'right',
                               'left', 'back', 'bottom'], face_vals.split()))

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

    def _revolve(self, direction):
        if direction == 'R':
            self.faces['front'], self.faces['left'], self.faces['back'], \
            self.faces['right'] = self.faces['right'], self.faces['front'], \
            self.faces['left'], self.faces['back']
        else:
            self.faces['front'], self.faces['left'], self.faces['back'], \
            self.faces['right'] = self.faces['left'], self.faces['back'], \
            self.faces['right'], self.faces['front']
            
    def show_right_face(self, top, front):
        if front == self.faces['back']:
            if top == self.faces['top']:
                self._revolve('R')
                self._revolve('R')
            else:
                self.roll('S')
                self.roll('S')
        elif front == self.faces['top']:
            self.roll('S')
        elif front == self.faces['right']:
            self._revolve('R')
        elif front == self.faces['left']:
            self._revolve('L')
        elif front == self.faces['bottom']:
            self.roll('N')
        if top == self.faces['bottom']:
            self.roll('E')
            self.roll('E')
        elif top == self.faces['right']:
            self.roll('W')
        elif top == self.faces['left']:
            self.roll('E')
        print(self.faces['right'])


import sys

face_vals = sys.stdin.readline()

dice = Dice(face_vals)

n = int(sys.stdin.readline())

for i in range(n):
    top, front = sys.stdin.readline().split()
    dice.show_right_face(top, front)