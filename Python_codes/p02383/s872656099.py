class Dice(object):
    
    def __init__(self, line):
        self.top = 1
        self.bottom = 6
        self.south = 2
        self.east = 3
        self.west = 4
        self.north = 5
        self.convert = line.split()
    
    def move(self, direction):
        if 'N' == direction:
            self.top, self.north, self.bottom, self.south = self.south, self.top, self.north, self.bottom
        elif 'S' == direction:
            self.top, self.north, self.bottom, self.south = self.north, self.bottom, self.south, self.top
        elif 'W' == direction:
            self.top, self.east, self.bottom, self.west = self.east, self.bottom, self.west, self.top
        elif 'E' == direction:
            self.top, self.east, self.bottom, self.west = self.west, self.top, self.east, self.bottom
    
    def result(self):
        return self.convert[self.top - 1]
    
dice = Dice(input())
for direction in input():
    dice.move(direction)

print(dice.result())