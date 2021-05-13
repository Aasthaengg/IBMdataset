class Dice:
    def __init__(self,pips):
        self.top = pips[0]
        self.south = pips[1]
        self.east = pips[2]
        self.west = pips[3]
        self.north =pips[4]
        self.bottom=pips[5]
    def n(self):
        self.top,self.south,self.bottom,self.north = \
        self.south,self.bottom,self.north,self.top
    def s(self):
        self.top,self.north,self.bottom,self.south = \
        self.north,self.bottom,self.south,self.top
    def e(self):
        self.top,self.west,self.bottom,self.east = \
        self.west,self.bottom,self.east,self.top
    def w(self):
        self.top,self.east,self.bottom,self.west = \
        self.east,self.bottom,self.west,self.top
    def r(self):
        self.north,self.east,self.south,self.west = \
        self.east,self.south,self.west,self.north
    def set(self,t,s):
        for i in range(4):
            if self.top != t:
                if self.east == t or self.west == t:
                    self.e()
                else:
                    self.n()
            else:
                break
        for i in range(4):
            if self.south != s:
                self.r()
            else:
                break

pips = [int(x) for x in input().split()]
a = Dice(pips)

n = int(input())
for i in range(n):
    t,s = map(int,input().split())
    a.set(t,s)
    print(a.east)