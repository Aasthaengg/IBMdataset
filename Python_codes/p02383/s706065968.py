class Dice():
    def __init__(self):
        self.nums = list(range(6))
        self.work = list(range(6))

    def set_nums(self, n0, n1, n2, n3, n4, n5):
        self.nums[0] = n0
        self.nums[1] = n1
        self.nums[2] = n2
        self.nums[3] = n3
        self.nums[4] = n4
        self.nums[5] = n5

    def rotate(self, cmd):
        for i in range(6):
            # deepcopy
            self.work[i] = self.nums[i]

        if cmd == 'N':
            self.set_nums(self.work[1], self.work[5], self.work[2], self.work[3], self.work[0], self.work[4])
        elif cmd == 'S':
            self.set_nums(self.work[4], self.work[0], self.work[2], self.work[3], self.work[5], self.work[1]),
        elif cmd == 'E':
            self.set_nums(self.work[3], self.work[1], self.work[0], self.work[5], self.work[4], self.work[2])
        else:
            self.set_nums(self.work[2], self.work[1], self.work[5], self.work[0], self.work[4], self.work[3])

    def top(self):
        return self.nums[0]

nums = [int(arg) for arg in input().split()]
d = Dice()
d.set_nums(*nums)
for cmd in list(input()):
    d.rotate(cmd)
print(d.top())

