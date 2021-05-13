class Dice:
    def __init__(self, nums):
        self.nums = nums
    def rotate(self, direction):
        nums = self.nums
        if direction=="E":
            self.nums = [nums[3], nums[1], nums[0], nums[5], nums[4], nums[2]]
        elif direction=="W":
            self.nums = [nums[2], nums[1], nums[5], nums[0], nums[4], nums[3]]
        elif direction=="N":
            self.nums = [nums[1], nums[5], nums[2], nums[3], nums[0], nums[4]]
        elif direction=="S":
            self.nums = [nums[4], nums[0], nums[2], nums[3], nums[5], nums[1]]

    def upper_num(self):
        return self.nums[0]

dice = Dice(list(map(int, input().split())))
dirs = list(input())
for i in range(len(dirs)):
    dice.rotate(dirs[i])

print(dice.upper_num())