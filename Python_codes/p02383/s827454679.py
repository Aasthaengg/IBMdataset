class Dice:
    def __init__(self, d):
        self.dice = d
        self.top = d[0]
        self.north = d[4]
        self.west = d[3]
        self.south = d[1]
        self.east = d[2]
        self.bottom = d[5]

    def move(self, d):
        if d == "N":
            self.move_north()
        elif d == "W":
            self.move_west()
        elif d == "S":
            self.move_south()
        elif d == "E":
            self.move_east()

    def move_north(self):
        self.top, self.south, self.bottom, self.north \
            = self.south, self.bottom, self.north, self.top

    def move_south(self):
        self.top, self.south, self.bottom, self.north \
            = self.north, self.top, self.south, self.bottom

    def move_east(self):
        self.top, self.east, self.bottom, self.west \
            = self.west, self.top, self.east, self.bottom

    def move_west(self):
        self.top, self.east, self.bottom, self.west \
            = self.east, self.bottom, self.west, self.top

if __name__ == "__main__":
    import re

    nums = [int(n) for n in re.split(r"\s+", input().strip())]
    dice = Dice(nums)

    for d in list(input().strip()):
        dice.move(d)

    print(dice.top)

