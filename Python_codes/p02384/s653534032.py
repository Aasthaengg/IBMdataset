class Dice:
    
    def __init__(self, nums):
        self.nums = list(nums)
        
    @property
    def top(self):
        return self.nums[0]
        
    def _shift(self, *pairs):
        for pair in pairs:
            num = self.nums[pair[0]]
            self.nums[pair[0]] = self.nums[pair[1]]
            self.nums[pair[1]] = num
            
    def go(self, opes:str):
        for ope in opes:
            if ope == "N":
                self.go_north()
            elif ope == "E":
                self.go_east()
            elif ope == "W":
                self.go_west()
            else:
                self.go_south()
                
    def go_top(self, num):
        i = self.nums.index(num)
        
        if i == 1:
            self.go_north()
        elif i == 2:
            self.go_west()
        elif i == 3:
            self.go_east()
        elif i == 4:
            self.go_south()
        elif i == 5:
            self.go_north()
            self.go_north()
            
    def go_ahead(self, num):
        i = self.nums.index(num)
        
        if i == 2:
            self.go_cw()
        elif i == 4:
            self.go_cw()
            self.go_cw()
        elif i == 3:
            self.go_ccw()
            
        
    def go_north(self):
        self._shift((0, 1), (1, 5), (5, 4))
        
    def go_east(self):
        self._shift((0, 3), (3, 5), (5, 2))
        
    def go_west(self):
        self._shift((0, 2), (2, 5), (5, 3))
        
    def go_south(self):
        self._shift((0, 4), (4, 5), (5, 1))
        
    def go_ccw(self):
        self._shift((3, 4), (4, 2), (2, 1))
        
    def go_cw(self):
        self._shift((3, 1), (1, 2), (2, 4))
        

dice = Dice(map(int, input().split()))

for _ in range(int(input())):
    top, ahead = map(int, input().split())
    dice.go_top(top)
    dice.go_ahead(ahead)
    print(dice.nums[2])
