class dice:
    men = [0] * 7
    def __init__(self, li):
        self.men = [0] + li
    def move0(self, a, b, c, d):
        self.men[a], self.men[b], self.men[c], self.men[d] = self.men[b], self.men[c], self.men[d], self.men[a]
    def move(self, h):
        if h == "N":
            self.move0(1, 2, 6, 5)
        elif h == "S":
            self.move0(1, 5, 6, 2)
        elif h == "W":
            self.move0(1, 3, 6, 4)
        elif h == "E":
            self.move0(1, 4, 6, 3)
    def move2(self, a, b):
        if self.men[1] != a:
            for i, ss in [(2, "N"), (3, "W"), (4, "E"), (5, "S"), (6, "NN")]:
                if self.men[i] == a:
                    for s in ss:
                        self.move(s)
                    break
        if self.men[2] != b:
            if b == self.men[3]:
                self.move0(2, 3, 5, 4)
            elif b == self.men[4]:
                self.move0(2, 4, 5, 3)
            else:
                self.men[2], self.men[5], self.men[3], self.men[4] = self.men[5], self.men[2], self.men[4], self.men[3]
saikoro = dice(list(map(int, input().split())))
for _ in range(int(input())):
    saikoro.move2(*map(int, input().split()))
    print(saikoro.men[3])

