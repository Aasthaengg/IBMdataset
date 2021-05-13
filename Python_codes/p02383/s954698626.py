num = list(map(int, input().split()))
A = input()

class Dice:
    def __init__(self, num):
        self.state = {}
        for i in range(1,6+1):
            self.state[i] = num[i-1]
        
    def action(self, a):
        new_state = self.state.copy()
        if a=='E':
            new_state[1] = self.state[4]
            new_state[4] = self.state[6]
            new_state[6] = self.state[3]
            new_state[3] = self.state[1]
        elif a=='N':
            new_state[1] = self.state[2]
            new_state[2] = self.state[6]
            new_state[6] = self.state[5]
            new_state[5] = self.state[1]
        elif a=='S':
            new_state[1] = self.state[5]
            new_state[5] = self.state[6]
            new_state[6] = self.state[2]
            new_state[2] = self.state[1]
        elif a=='W':
            new_state[1] = self.state[3]
            new_state[3] = self.state[6]
            new_state[6] = self.state[4]
            new_state[4] = self.state[1]
        self.state = new_state
    
dice = Dice(num)
for a in A:
    dice.action(a)

print(dice.state[1])
