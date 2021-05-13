class Dice:
    def __init__(self, f):
        self.f = f

    def roll(self, s):
        for f in s:
            n = self.f[:]
            if f == 'E':
                t = n[0]
                n[0] = n[3]
                n[3] = n[5]
                n[5] = n[2]
                n[2] = t
            elif f == 'W':
                t = n[0]
                n[0] = n[2]
                n[2] = n[5]
                n[5] = n[3]
                n[3] = t
            elif f == 'N':
                t = n[0]
                n[0] = n[1]
                n[1] = n[5]
                n[5] = n[4]
                n[4] = t
            else:
                t = n[0]
                n[0] = n[4]
                n[4] = n[5]
                n[5] = n[1]
                n[1] = t
            self.f = n

    def top(self):
        return self.f[0]

d = Dice(list(map(int, input().split())))
r = input()
d.roll(r)
print(d.top())