class Dice():
    #0:上面、1:前面、2:側面(見える方)、3:側面(裏側)、4:背面、5:底面
    def __init__(self,numlist):
        self.lst=numlist
    
    def roll(self,direction):
        for x in direction:
            if x=="S" : self.lst=[self.lst[4],self.lst[0],self.lst[2],self.lst[3],self.lst[5],self.lst[1]]
            elif x=="N" : self.lst=[self.lst[1],self.lst[5],self.lst[2],self.lst[3],self.lst[0],self.lst[4]]
            elif x=="W" : self.lst=[self.lst[2],self.lst[1],self.lst[5],self.lst[0],self.lst[4],self.lst[3]]
            elif x=="E" : self.lst=[self.lst[3],self.lst[1],self.lst[0],self.lst[5],self.lst[4],self.lst[2]]        
    
    def dice_set_make(self):
        self.dice_set=[]
        for x in ["","W","WW","WWW","SE","SW"]:
            self.work=Dice(self.lst[:])
            self.work.roll(x)
            self.dice_set.append(self.work.lst)
            for _ in range(3):
                self.work.roll("S")
                self.dice_set.append(self.work.lst)
        

lst=list(map(int,input().split()))
q=int(input())

d1=Dice(lst)
d1.dice_set_make()
dice_set=d1.dice_set

for _ in range(q):
    a,b=map(int,input().split())
    for x in dice_set:
        if x[0]==a and x[1]==b:
            print(x[2])
            break
