import copy

class Dice:
    def __init__(self,numbers): 
        self.numbers=numbers

    def movement(self,direction):
        tmp=copy.copy(self.numbers)
        if(direction=="E"):
            self.numbers[0]=tmp[3]
            self.numbers[2]=tmp[0]
            self.numbers[3]=tmp[5]
            self.numbers[5]=tmp[2]
        elif(direction=="S"):
            self.numbers[0]=tmp[4]
            self.numbers[1]=tmp[0]
            self.numbers[4]=tmp[5]
            self.numbers[5]=tmp[1]
        elif(direction=="W"):
            self.numbers[0]=tmp[2]
            self.numbers[2]=tmp[5]
            self.numbers[3]=tmp[0]
            self.numbers[5]=tmp[3]
        elif(direction=="N"):
            self.numbers[0]=tmp[1]
            self.numbers[1]=tmp[5]
            self.numbers[4]=tmp[0]
            self.numbers[5]=tmp[4]
    
    def top(self):
        return self.numbers[0]

numbers=list(map(int,input().split(" ")))
d=Dice(numbers)

comms=list(input())
for comm in comms:
    d.movement(comm)

print(d.top())
