class Dice:
    def __init__(self):
        # top, front, right, left, back, bottom
        self.numbers = map(int, raw_input().split())
    
    @property
    def top(self):
        return self.numbers[0]
    
    @property
    def front(self):
        return self.numbers[1]
        
    @property
    def right(self):
        return self.numbers[2]
        
    @property
    def left(self):
        return self.numbers[3]
    
    @property
    def back(self):
        return self.numbers[4]
        
    @property
    def bottom(self):
        return self.numbers[5]

    def roll(self, direction):
        if direction == "N":
            before_inds = [0, 1, 5, 4]
            after_inds  = [1, 5, 4, 0]
        elif direction == "S":
            before_inds = [0, 1, 5, 4]
            after_inds  = [4, 0, 1, 5]
        elif direction == "E":
            before_inds = [0, 2, 5, 3]
            after_inds  = [3, 0, 2, 5]
        elif direction == "W":
            before_inds = [0, 2, 5, 3]
            after_inds  = [2, 5, 3, 0]
        else:
            return False
        changed = [self.numbers[i] for i in after_inds]
        for c_i, n_i in enumerate(before_inds):
            self.numbers[n_i] = changed[c_i]
        return True
        
dice = Dice()
for d in raw_input():
    dice.roll(d)
    
print dice.top