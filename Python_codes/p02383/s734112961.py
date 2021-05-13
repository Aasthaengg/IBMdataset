class Dice:
    def __init__(self, n1, n2, n3, n4, n5, n6):
        self.elements = [n1, n2, n3, n4, n5, n6]

    def rotateW(self):
        n5 = self.elements[0]
        n1 = self.elements[2]
        n3 = self.elements[5]
        n6 = self.elements[4]
        self.elements[4] = n5
        self.elements[0] = n1
        self.elements[2] = n3
        self.elements[5] = n6

    def rotateN(self):
        n2 = self.elements[0]
        n1 = self.elements[3]
        n4 = self.elements[5]
        n6 = self.elements[1]
        self.elements[1] = n2
        self.elements[0] = n1
        self.elements[3] = n4
        self.elements[5] = n6


    def rotateS(self):
        n4 = self.elements[0]
        n1 = self.elements[1]
        n2 = self.elements[5]
        n6 = self.elements[3]
        self.elements[3] = n4
        self.elements[0] = n1
        self.elements[1] = n2
        self.elements[5] = n6

    def rotateE(self):
        n3 = self.elements[0]
        n1 = self.elements[4]
        n5 = self.elements[5]
        n6 = self.elements[2]
        self.elements[2] = n3
        self.elements[0] = n1
        self.elements[4] = n5
        self.elements[5] = n6

elements = map(int, raw_input().split(" "))
dice = Dice(elements[0], elements[4], elements[2], elements[1], elements[3], elements[5])
rule = raw_input()

for i in rule:
    if i == "S": dice.rotateS()
    elif i == "W": dice.rotateW()
    elif i == "N": dice.rotateN()
    elif i == "E": dice.rotateE()

print(str(dice.elements[0]))