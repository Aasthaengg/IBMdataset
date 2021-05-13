n = [int(i) for i in input().split()]
s = input()


class Dice(object):
    def __init__(self,num):
        self.n = num[4]
        self.e = num[2]
        self.w = num[3]
        self.s = num[1]
        self.center = num[0]
        self.back = num[5]

    def move(self,str):
        if str == 'N':
            x = self.n
            self.n = self.center
            self.center = self.s
            self.s = self.back
            self.back = x
            return self.center
        elif str == 'S':
            x = self.s
            self.s = self.center
            self.center = self.n
            self.n = self.back
            self.back = x
            return self.center
        elif str== 'E':
            x = self.e
            self.e = self.center
            self.center = self.w
            self.w = self.back
            self.back = x
            return self.center
        elif str == 'W':
            x = self.w
            self.w = self.center
            self.center = self.e
            self.e = self.back
            self.back = x
            return self.center

dice = Dice(n)
status = 0

for i in range(len(s)):
    status = dice.move(s[i])

print(status)