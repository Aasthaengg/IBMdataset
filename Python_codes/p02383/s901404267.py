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
        
    def go_north(self):
        self._shift((0, 1), (1, 5), (5, 4))
        
    def go_east(self):
        self._shift((0, 3), (3, 5), (5, 2))
        
    def go_west(self):
        self._shift((0, 2), (2, 5), (5, 3))
        
    def go_south(self):
        self._shift((0, 4), (4, 5), (5, 1))
        

dice = Dice(map(int, input().split()))
dice.go(input())
print(dice.top)
