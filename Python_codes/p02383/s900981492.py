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
        self.order_seq = order_seq
        for _, order in enumerate(self.order_seq):
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
        
numbers = list(map(int, input().split()))
order_seq = list(input())

dice = Dice(numbers)
print(dice.order(order_seq))
