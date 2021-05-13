class Dice:
    def __init__(self, d1, d2, d3, d4, d5, d6):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
 
    def output(self, a, b):
        if (a == self.d1 and b == self.d2) or (a == self.d2 and b == self.d6) \
         or (a == self.d6 and b == self.d5) or (a == self.d5 and b == self.d1):
            print(self.d3)
        elif (a == self.d2 and b == self.d1) or (a == self.d6 and b == self.d2) \
         or (a == self.d5 and b == self.d6) or (a == self.d1 and b == self.d5):
            print(self.d4)
        elif (a == self.d1 and b == self.d3) or (a == self.d3 and b == self.d6) \
         or (a == self.d6 and b == self.d4) or (a == self.d4 and b == self.d1):
            print(self.d5)
        elif (a == self.d3 and b == self.d1) or (a == self.d6 and b == self.d3) \
         or (a == self.d4 and b == self.d6) or (a == self.d1 and b == self.d4):
            print(self.d2)
        elif (a == self.d2 and b == self.d3) or (a == self.d3 and b == self.d5) \
         or (a == self.d5 and b == self.d4) or (a == self.d4 and b == self.d2):
            print(self.d1)
        elif (a == self.d3 and b == self.d2) or (a == self.d5 and b == self.d3) \
         or (a == self.d4 and b == self.d5) or (a == self.d2 and b == self.d4):
            print(self.d6)  

d1, d2, d3, d4, d5, d6 = map(int, input().split())
dice = Dice(d1, d2, d3, d4, d5, d6)
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    dice.output(a, b)
