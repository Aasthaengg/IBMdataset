# 1: top, 2: front, 3: right,
# 4: left, 5: back, 6: bottom

class Dice:
    def __init__(self, nums):
        self.top, self.front, self.right, self.left, self.back, self.bottom = nums

    def roll(self, direction):
        if direction == 'E':
            self.top, self.right, self.left, self.bottom = self.left, self.top, self.bottom, self.right
            return

        if direction == 'N':
            self.top, self.front, self.back, self.bottom = self.front, self.bottom, self.top, self.back
            return

        if direction == 'S':
            self.top, self.front, self.back, self.bottom = self.back, self.top, self.bottom, self.front
            return

        if direction == 'W':
            self.top, self.right, self.left, self.bottom = self.right, self.bottom, self.top, self.left
            return

    def get_top(self):
        return self.top

if __name__ == '__main__':
    nums = [int(i) for i in input().split()]
    directions = input()

    d = Dice(nums)
    for ch in directions:
        d.roll(ch)

    print(d.get_top())