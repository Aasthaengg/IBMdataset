from collections import deque

class Dice:
    def __init__(self, top, down, right, left, up, bottom):
        self.top = top
        self.bottom = bottom
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def roll(self, command):
        for c in list(command):
            if c == 'N':
                self.up, self.top, self.down, self.bottom = self.top, self.down, self.bottom, self.up
            elif c == 'S':
                self.up, self.top, self.down, self.bottom = self.bottom, self.up, self.top, self.down
            elif c == 'E':
                self.left, self.top, self.right, self.bottom = self.bottom, self.left, self.top, self.right
            elif c == 'W':
                self.left, self.top, self.right, self.bottom = self.top, self.right, self.bottom, self.left

    def pip(self):
        return self.top

if __name__ == '__main__':
    seq = list(map(int, input().split()))
    dice = Dice(*seq)
    dice.roll(input())
    print(dice.pip())

