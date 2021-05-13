from sys import stdin

class Dice:
    def __init__(self, nums):
        self.labels = {
            "1" : nums[0],
            "2" : nums[1],
            "3" : nums[2],
            "4" : nums[3],
            "5" : nums[4],
            "6" : nums[5]
        }
        self.pos = {
            "E" : "3",
            "W" : "4",
            "S" : "2",
            "N" : "5",
            "T" : "1",
            "B" : "6"
        }

    def roll(self, query):
        for q in query:
            if q == "E":
                self.pos["T"], self.pos["E"], self.pos["B"], self.pos["W"] = self.pos["W"], self.pos["T"], self.pos["E"], self.pos["B"]
            elif q == "W":
                self.pos["T"], self.pos["E"], self.pos["B"], self.pos["W"] = self.pos["E"], self.pos["B"], self.pos["W"], self.pos["T"]
            elif q == "S":
                self.pos["T"], self.pos["S"], self.pos["B"], self.pos["N"] = self.pos["N"], self.pos["T"], self.pos["S"], self.pos["B"]
            elif q == "N":
                self.pos["T"], self.pos["S"], self.pos["B"], self.pos["N"] = self.pos["S"], self.pos["B"], self.pos["N"], self.pos["T"]

nums = [int(x) for x in stdin.readline().rstrip().split()]
queries = stdin.readline().rstrip()
d = Dice(nums)
d.roll(queries)
print(d.labels[d.pos["T"]])
