class Dice:
    """????????????????????????"""
    def __init__(self, s):
        self.s1 = s[0]
        self.s2 = s[1]
        self.s3 = s[2]
        self.s4 = s[3]
        self.s5 = s[4]
        self.s6 = s[5]

    def roll(self, direction):          # ???????????????????§??????¢????????¢
        temp = self.s1
        if direction == "E":
            self.s1 = self.s4
            self.s4 = self.s6
            self.s6 = self.s3
            self.s3 = temp
        elif direction == "N":
            self.s1 = self.s2
            self.s2 = self.s6
            self.s6 = self.s5
            self.s5 = temp
        elif direction == "S":
            self.s1 = self.s5
            self.s5 = self.s6
            self.s6 = self.s2
            self.s2 = temp
        elif direction == "W":
            self.s1 = self.s3
            self.s3 = self.s6
            self.s6 = self.s4
            self.s4 = temp

    def setposition(self, a, b):
        while 1:
            if self.s1 == a:
                break
            self.roll("N")
            if self.s1 == a:
                break
            self.roll("E")
        while 1:
            if self.s2 == b:
                break
            self.roll("N")
            self.roll("E")
            self.roll("S")


s = list(map(int, input().split()))
dice1 = Dice(s)
q = int(input())

for _ in range(q):
    a, b = map(int, input().split())
    dice1.setposition(a, b)
    print(dice1.s3)