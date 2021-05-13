class Dice:
    def __init__(self, dice):
        self.dice = dice
        self.face = {'head':1, 'tail':4, 'left':3, 'right':2, 'above':0, 'below':5}
    
    def roll(self, ch):
        dice = self.dice
        face = self.face
        if ch == 'S':
            tmp = dice[face['head']]
            dice[face['head']] = dice[face['above']]
            dice[face['above']] = dice[face['tail']]
            dice[face['tail']] = dice[face['below']]
            dice[face['below']] = tmp
        elif ch == 'N':
            tmp = dice[face['head']]
            dice[face['head']] = dice[face['below']]
            dice[face['below']] = dice[face['tail']]
            dice[face['tail']] = dice[face['above']]
            dice[face['above']] = tmp
        elif ch == 'W':
            tmp = dice[face['left']]
            dice[face['left']] = dice[face['above']]
            dice[face['above']] = dice[face['right']]
            dice[face['right']] = dice[face['below']]
            dice[face['below']] = tmp
        else:
            tmp = dice[face['left']]
            dice[face['left']] = dice[face['below']]
            dice[face['below']] = dice[face['right']]
            dice[face['right']] = dice[face['above']]
            dice[face['above']] = tmp

    def top(self):
        dice = self.dice
        face = self.face
        return dice[face['above']]
    
    def find_right(self, a, b):
        dice = self.dice
        face = self.face
        order = 'NNNNWNNNWNNNENNNENNNWNNN'
        for ch in order:
            self.roll(ch)
            if dice[face['above']] == a and dice[face['head']] == b:
                break
        return dice[face['right']]

dice = Dice([*map(int, input().split())])
q = int(input())
while q > 0:
    q -= 1
    a, b = map(int, input().split())
    print(dice.find_right(a, b))
