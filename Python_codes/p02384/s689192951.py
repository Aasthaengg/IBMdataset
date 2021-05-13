class Dice:
    def __init__(self, num):
        self.num = num
    def roll(self, fn):
        if fn == "S":
            ue = self.num[4]
            self.num[4] = self.num[5]
            self.num[5] = self.num[1]
            self.num[1] = self.num[0]
            self.num[0] = ue
        elif fn == "W":
            ue = self.num[2]
            self.num[2] = self.num[5]
            self.num[5] = self.num[3]
            self.num[3] = self.num[0]
            self.num[0] = ue        
        elif fn == "N":
            ue = self.num[1]
            self.num[1] = self.num[5]
            self.num[5] = self.num[4]
            self.num[4] = self.num[0]
            self.num[0] = ue                
 
    def spin(self, fn):
        if fn == "migi":
            mae = self.num[3]
            self.num[3] = self.num[4]
            self.num[4] = self.num[2]
            self.num[2] = self.num[1]
            self.num[1] = mae
num = list(map(int, input().split(" ")))
dice1 = Dice(num)
n = int(input())
a = []
for i in range(n):
    u, f = map(int, input().split(" "))
    count = 0
    while num[0] != u and count<5:
        dice1.roll("S")
        count+=1
    count = 0
    while num[0] != u and count<5:
        dice1.roll("W")
        count+=1        
    while num[1] != f:
        dice1.spin("migi")
    a.append(num[2])
for i in range(n):
    print(a[i])
    
