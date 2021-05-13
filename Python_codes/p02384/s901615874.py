class dice:
    def __init__(self,A):
        self.side = {
            "TOP":A[0],
            "S":A[1],
            "E":A[2],
            "W":A[3],
            "N":A[4],
            "BOT":A[5],
            }
        self.reverse = {
            "E":"W",
            "W":"E",
            "S":"N",
            "N":"S"}
        
    def main(self,A):
        for s in A:
            var = int(self.side[s])
            self.side[s] = self.side["TOP"]
            self.side["TOP"] = self.side[self.reverse[s]]
            self.side[self.reverse[s]] = self.side["BOT"]
            self.side["BOT"] = var
        # print("{}".format(self.side["TOP"]))
    def rotate(self,top,flont):
        if self.side["TOP"] != top:
            if self.side["BOT"] == top:
                self.main("NN")
            elif self.side["N"] == top:
                self.main("S")
            elif self.side["S"] == top:
                self.main("N")
            elif self.side["E"] == top:
                self.main("W")
            elif self.side["W"] == top:
                self.main("E")
        for x in range(4):
            if self.side["S"] == flont:
                break
            else:
                var = int(self.side["N"])
                self.side["N"] = self.side["E"]
                self.side["E"] = self.side["S"]
                self.side["S"] = self.side["W"]
                self.side["W"] = var
        print(self.side["E"])

var = dice(list(map(int,input().split())))
# var.main(input())
num = int(input())
for n in range(num):
    top,front = map(int,input().split())
    var.rotate(top,front)
