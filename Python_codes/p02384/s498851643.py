class Dice2():

    def __init__(self, v): # v [Top, Front, Right, Left, Back, Bottom ]
        self.view = v
        self.dTFR = {}
        for i, j, k in ((ii, (ii++2)%6, (ii+4)%6) for ii in  range(6)):
            self.dTFR[self.view[i]]=[self.view[v] for v in (j, k, 5-j, 5-k, j)]


d2, q = Dice2(list(map(int, input().split()))), int(input())
for i in range(q):
    t, f = map(int, input().split())
    print(d2.dTFR[t][d2.dTFR[t].index(f)+1] )