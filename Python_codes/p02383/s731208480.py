import sys
class Dice:
    def __init__(self):
        #self.ms = ms
        self.number = [i for i in range(6)]
        self.dev = [i for i in range(6)]
    
    def set_num(self,n0,n1,n2,n3,n4,n5):
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5
   
    def dice_roll(self,event):
        for i in range(6):
            self.dev[i] = self.number[i]
        #0:上,1:南,2:東,3:西,4:北,5:下
        if event == "S":
            self.set_num(self.dev[4],self.dev[0],self.dev[2],self.dev[3],self.dev[5],self.dev[1])
        if event == "N":
            self.set_num(self.dev[1],self.dev[5],self.dev[2],self.dev[3],self.dev[0],self.dev[4])
        if event == "E":
            self.set_num(self.dev[3],self.dev[1],self.dev[0],self.dev[5],self.dev[4],self.dev[2])
        if event == "W":
            self.set_num(self.dev[2],self.dev[1],self.dev[5],self.dev[0],self.dev[4],self.dev[3])
    
    def get_top(self):
        #for i in range(len(self.number)):
            #print(self.number[i])
        #sys.exit()
        return self.number[0]

ms = list(map(int,input().split()))
dice = Dice()
dice.set_num(ms[0],ms[1],ms[2],ms[3],ms[4],ms[5])
events = list(str(input()))
for event in events:
    dice.dice_roll(event)

print(dice.get_top())
