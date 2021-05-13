class Dice():
    def __init__(self, numbers):
        self.top = numbers[0]
        self.s = numbers[1]
        self.e = numbers[2]
        self.w = numbers[3]
        self.n = numbers[4]
        self.bot = numbers[5]
    def rot(self, dir):
        top, s, e, w, n, bot = (self.top, self.s, self.e, self.w, self.n, self.bot)
        if dir == 'N':
            self.top = s
            self.s = bot
            self.e = e
            self.w = w
            self.n = top
            self.bot = n
        elif dir == 'S':
            self.top = n
            self.s = top
            self.e = e
            self.w = w
            self.n = bot
            self.bot = s
        elif dir == 'E':
            self.top = w
            self.s = s
            self.e = top
            self.w = bot
            self.n = n
            self.bot = e
        elif dir == 'W':
            self.top = e
            self.s = s
            self.e = bot
            self.w = top
            self.n = n
            self.bot = w
    def getTop(self):
        return self.top
    def rotMany(self, command):
        for dir in command:
            self.rot(dir)



li = list(map(int, input().split()))
D = Dice(li)
n = int(input())
for _ in range(n):
    t, s = map(int, input().split())
    for cmd in ["N","N","N","E","EE",""]:
        if D.top == t:
            break
        else:
            D.rotMany(cmd)
    for cmd in ["SEN", "SEN", "SEN", ""]:
        if D.s == s:
            break
        else:
            D.rotMany(cmd)
    print(D.e)

