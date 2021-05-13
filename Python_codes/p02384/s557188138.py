import random

class Dice():
    def __init__(self, number):
        self.number = number

    def S(self):
        temp = self.number
        self.number = [temp[4], temp[0], temp[2], temp[3], temp[5], temp[1]]

    def N(self):
        temp = self.number
        self.number = [temp[1], temp[5], temp[2], temp[3], temp[0], temp[4]]

    def E(self):
        temp = self.number
        self.number = [temp[3], temp[1], temp[0], temp[5], temp[4], temp[2]]

    def W(self):
        temp = self.number
        self.number = [temp[2], temp[1], temp[5], temp[0], temp[4], temp[3]]

    def order(self, str):
        for ch in str:
            if ch == "S":
                self.S()
            elif ch == "N":
                self.N()
            elif ch == "E":
                self.E()
            else:
                self.W()

    def query(self, top, front):
        while True:
            drc = random.randint(0, 3)
            self.order("NEWS"[drc])
            if self.number[0] == top and self.number[1] == front:
                return self.number[2]
                break

number = list(map(int, input().split()))
q = int(input())
dice = Dice(number)

for i in range(q):
    t, f = map(int, input().split())
    print(dice.query(t, f))
