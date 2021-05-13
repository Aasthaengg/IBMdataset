class Dice():
    def __init__(self,numlist):
        self.lst=numlist
    
    def roll(self,direction):
        if direction=="S" : self.lst=[self.lst[4],self.lst[0],self.lst[2],self.lst[3],self.lst[5],self.lst[1]]
        elif direction=="N" : self.lst=[self.lst[1],self.lst[5],self.lst[2],self.lst[3],self.lst[0],self.lst[4]]
        elif direction=="W" : self.lst=[self.lst[2],self.lst[1],self.lst[5],self.lst[0],self.lst[4],self.lst[3]]
        elif direction=="E" : self.lst=[self.lst[3],self.lst[1],self.lst[0],self.lst[5],self.lst[4],self.lst[2]]        

lst=list(map(int,input().split()))
directions=input()

d1=Dice(lst)
for direction in directions:
    d1.roll(direction)

print(d1.lst[0])
