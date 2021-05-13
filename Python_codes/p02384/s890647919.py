class Dice(object):

    def __init__(self, n):
        self.n = n
        self.pos = ['12431', '03520', '01540', '04510', '02530', '13421']

    def face(self, x1, x2):
        s = '{0}{1}'.format(self.n.index(x1),self.n.index(x2))
        for i, p in enumerate(self.pos):
            if s in p:
                return self.n[i]
dice = Dice([int(i) for i in input().split()])
n = int(input())
for _ in range(n):
    x1, x2 = map(int, input().split())
    print(dice.face(x1, x2))


