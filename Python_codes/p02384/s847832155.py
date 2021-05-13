class Dice:
    def __init__(self, numbers):
        self.dice = {"上" :numbers[0],
                     "下":numbers[5], 
                     "前":numbers[1],
                     "後":numbers[4],
                     "左":numbers[3],
                     "右":numbers[2]
                    }
    
    def order(self, order_seq):
        for _, order in enumerate(order_seq):
            if order == "N":
                self.north()
            elif order == "E":
                self.east()
            elif order == "W":
                self.west()
            elif order == "S":
                self.south()
        
        return self.dice["上"]

    def north(self):
        U, D, F, B = [self.dice["上"], self.dice["下"], self.dice["前"], self.dice["後"]]
        self.dice["上"] = F
        self.dice["前"] = D
        self.dice["下"] = B
        self.dice["後"] = U

    def east(self):
        U, D, L, R = [self.dice["上"], self.dice["下"], self.dice["左"], self.dice["右"]]
        self.dice["上"] = L
        self.dice["下"] = R
        self.dice["左"] = D
        self.dice["右"] = U

    def west(self):
        U, D, L, R = [self.dice["上"], self.dice["下"], self.dice["左"], self.dice["右"]]
        self.dice["上"] = R
        self.dice["下"] = L
        self.dice["左"] = U
        self.dice["右"] = D

    def south(self):
        U, D, F, B = [self.dice["上"], self.dice["下"], self.dice["前"], self.dice["後"]]
        self.dice["上"] = B
        self.dice["前"] = U
        self.dice["下"] = F
        self.dice["後"] = D   

    def set_position(self, n, position_seq):
        self.ans = []
        for i in range(n):
            self.up = position_seq[i][0]
            self.front = position_seq[i][1]
            
            self.search()
            self.west()
            self.search()
            self.west()
            self.search()
            self.north()
            self.search()
            self.west()
            self.search()
            self.west()
            self.search()
        
        return self.ans
    
    def search(self):
        # print("goal:now", self.up, ":", self.dice["上"])
        if self.dice["上"] == self.up:
            for _ in range(4):
                # print("goal:now|up ", self.front, ":", self.dice["前"], "|", self.dice["上"], "→", self.dice["右"])
                if self.dice["前"] == self.front:
                    break
                self.rotate()
            self.ans.append(self.dice["右"])

    def rotate(self):
        F, R, B, L = [self.dice["前"], self.dice["右"], self.dice["後"], self.dice["左"]]
        self.dice["前"] = R
        self.dice["右"] = B
        self.dice["後"] = L
        self.dice["左"] = F
        
numbers = list(map(int, input().split()))
n = int(input())
pos_seq = []
for _ in range(n):
    pos_seq.append(list(map(int, input().split())))

dice = Dice(numbers)
ans = dice.set_position(n, position_seq = pos_seq)
for i in range(n):
    print(ans[i])
