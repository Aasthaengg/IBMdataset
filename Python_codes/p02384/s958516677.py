class Dice():
    def __init__(self, nums):
        self.nums = nums
        self.top, self.front, self.right = 0, 1, 2

    def move(self, op):
        for c in op:
            if c == 'N':
                self.top, self.front = self.front, 5 - self.top
            elif c == 'S':
                self.top, self.front = 5 - self.front, self.top
            elif c == 'E':
                self.top, self.right = 5 - self.right, self.top
            else:
                self.top, self.right = self.right, 5 - self.top

    def getRight(self, t, f):
        top, front = self.nums.index(t), self.nums.index(f)
        for c in "NNNNEEE":
            self.move(c)
            if top == self.top:
                break
        while True:
            self.move("ESW")
            if front == self.front:
                return self.nums[self.right]

dice = Dice([int(n) for n in input().split()])
n = int(input())
for _ in range(n):
    t, f = [int(x) for x in input().split()]
    print(dice.getRight(t, f))