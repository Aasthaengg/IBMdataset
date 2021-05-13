class Dice:
    def __init__(self, men):
        self.men = men

    def throw(self, direction):
        if direction == "E":
            pmen = men[:]
            men[0] = pmen[3]
            men[1] = pmen[1]
            men[2] = pmen[0]
            men[3] = pmen[5]
            men[4] = pmen[4]
            men[5] = pmen[2]
        elif direction == "W":
            pmen = men[:]
            men[0] = pmen[2]
            men[1] = pmen[1]
            men[2] = pmen[5]
            men[3] = pmen[0]
            men[4] = pmen[4]
            men[5] = pmen[3]
        elif direction == "S":
            pmen = men[:]
            men[0] = pmen[4]
            men[1] = pmen[0]
            men[2] = pmen[2]
            men[3] = pmen[3]
            men[4] = pmen[5]
            men[5] = pmen[1]
        elif direction == "N":
            pmen = men[:]
            men[0] = pmen[1]
            men[1] = pmen[5]
            men[2] = pmen[2]
            men[3] = pmen[3]
            men[4] = pmen[0]
            men[5] = pmen[4]


    def printUe(self):
        print (self.men)[0]

    def printMigi(self):
        print (self.men)[2]

    def printMen(self):
        print self.men


men = map(int, (raw_input()).split(" "))
d = Dice(men)

q = int(raw_input())

for i in range(q):
    Q = map(int, (raw_input()).split(" "))
    if(d.men[2] == Q[1] or d.men[3] == Q[1]):
        d.throw("E")

    while(d.men[1] != Q[1]):
        d.throw("S")

    while(d.men[0] != Q[0]):
        d.throw("E")

    d.printMigi()