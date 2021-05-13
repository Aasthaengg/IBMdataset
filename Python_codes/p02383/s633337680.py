class Dice:
    def __init__(self):
        self.dice=[i for i in range(6)]
        self.workspace=[i for i in range(6)]
        self.top=self.dice=[0]
    
    def set(self,numbers):
        self.dice=[i for i in numbers]
        self.workspace=[i for i in numbers]
        
    def rotate(self,command):
        if command == "W":
            self.workspace=[self.dice[2], self.dice[1], self.dice[5], self.dice[0], self.dice[4], self.dice[3]]
            self.dice=self.workspace
        elif command == "E":
            self.workspace=[self.dice[3], self.dice[1], self.dice[0], self.dice[5], self.dice[4], self.dice[2]]
            self.dice = self.workspace
        
        if command == "S":
            self.workspace=[self.dice[4], self.dice[0], self.dice[2], self.dice[3], self.dice[5], self.dice[1]]
            self.dice=self.workspace
        elif command == "N":
            self.workspace=[self.dice[1], self.dice[5], self.dice[2], self.dice[3], self.dice[0], self.dice[4]]
            self.dice=self.workspace
            
    def get_top(self):
        self.top=self.dice[0]
        print(self.top)
        
    def debug(self,numbers):
        print(numbers)
    
        
numbers=list(map(int,input().split()))
dice=Dice()
dice.set(numbers)
commands=input()
for i in range(len(commands)):
      dice.rotate(commands[i])
dice.get_top()
