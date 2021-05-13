class Dice:
    def __init__(self, top, front, right, left, back, bottom):
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.back = back
        self.bottom = bottom

    def N(self):
        save = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = self.back
        self.back = save

    def E(self):
        save = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = save

    def S(self):
        save = self.top
        self.top = self.back
        self.back = self.bottom
        self.bottom = self.front
        self.front = save

    def W(self):
        save = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = save

    def display(self):
        print(self.top)

nums = list(map(int, input().split()))
dice = Dice(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
s = input()
for c in s:
    if c == 'N':
        dice.N()
    elif c == 'E':
        dice.E()
    elif c == 'S':
        dice.S()
    elif c == 'W':
        dice.W()
dice.display()
