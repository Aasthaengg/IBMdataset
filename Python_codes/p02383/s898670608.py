# coding: utf-8
# Your code here!

class Dice:
    def __init__(self,lst):
        self.face=lst
    
    def roll(self,x):
        tmp=self.face
        if x=="E":
            self.face=[tmp[3],tmp[1],tmp[0],tmp[5],tmp[4],tmp[2]]
        if x=="W":
            self.face=[tmp[2],tmp[1],tmp[5],tmp[0],tmp[4],tmp[3]]
        if x=="N":
            self.face=[tmp[1],tmp[5],tmp[2],tmp[3],tmp[0],tmp[4]]
        if x=="S":
            self.face=[tmp[4],tmp[0],tmp[2],tmp[3],tmp[5],tmp[1]]
    
    def showDown(self):
        return self.face[0]
    
dice=Dice(list(map(int,input().split(" "))))
rolling=list(input())
for i in rolling:
    dice.roll(i)
print(dice.showDown())
