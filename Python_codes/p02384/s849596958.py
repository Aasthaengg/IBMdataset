class Dice:
    def __init__(self, f):
        self.f = f[:]

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

    def to_top(self, index):
        if index == 1:
            self.roll('N')
        elif index == 2:
            self.roll('W')
        elif index == 3:
            self.roll('E')
        elif index == 4:
            self.roll('S')
        elif index == 5:
            self.roll('NN')

    def side_roll(self):
        t  = self.f[1]
        self.f[1] = self.f[2]
        self.f[2] = self.f[4]
        self.f[4] = self.f[3]
        self.f[3] = t

    def top(self):
        return self.f[0]

    def front(self):
        return self.f[1]

    def r(self):
        return self.f[2]

df = list(input().split())
q = int(input())
for _ in range(q):
    d = Dice(df)
    t, f = input().split()
    ti = d.f.index(t)
    fi = d.f.index(f)
    d.to_top(ti)
    while d.front() != f:
        d.side_roll()
    print(d.r())