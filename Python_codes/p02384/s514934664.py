class Dice():
    def __init__(self, up, back, right, left, front, down):
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.front = front
        self.back = back
    
    def north(self):
        temp = self.up
        self.up = self.back
        self.back = self.down
        self.down = self.front
        self.front = temp
    
    def south(self):
        temp = self.up
        self.up = self.front
        self.front = self.down
        self.down = self.back
        self.back = temp
        
    def east(self):
        temp = self.up
        self.up = self.left
        self.left = self.down
        self.down = self.right
        self.right = temp
    
    def west(self):
        temp = self.up
        self.up = self.right
        self.right = self.down
        self.down = self.left
        self.left = temp
    
    def counterclockwise(self):
        temp = self.back
        self.back = self.left
        self.left = self.front
        self.front = self.right
        self.right = temp
    
    def clockwise(self):
        temp = self.back
        self.back = self.right
        self.right = self.front
        self.front = self.left
        self.left = temp
        
    def operate(self, op):
        if op == "N":
            self.north()
        elif op == "S":
            self.south()
        elif op == "E":
            self.east()
        elif op == "W":
            self.west()
        
    def fix_up(self, up):
        if self.down == up:
            self.north()
            self.north()
        elif self.right == up:
            self.west()
        elif self.left == up:
            self.east()
        elif self.front == up:
            self.south()
        elif self.back == up:
            self.north()

    def fix_back_with_fixed_up(self, back):
        if self.right == back:
            self.clockwise()
        elif self.left == back:
            self.counterclockwise()
        elif self.front == back:
            self.clockwise()
            self.clockwise()

up, back, right, left, front, down = map(int, input().split())
dice = Dice(up, back, right, left, front, down)

question_n = int(input())
for _ in range(question_n):
    q_up, q_back = map(int, input().split())
    dice.fix_up(q_up)
    dice.fix_back_with_fixed_up(q_back)
    print(dice.right)
