class dice:
    def __init__(self,label):
        self.top,self.front,self.right,self.left,self.rear,self.bottom\
            = label
    def roll(self, order):
        if order== "N":
            self.top, self.front, self.bottom, self.rear \
                = self.front, self.bottom, self.rear, self.top
        elif order=="E":
            self.top, self.left, self.bottom, self.right\
                = self.left, self.bottom, self.right, self.top
        elif order=="W":
            self.top, self.right, self.bottom, self.left\
                = self.right, self.bottom, self.left, self.top
        elif order=="S":
            self.top, self.rear, self.bottom, self.front\
                = self.rear,self.bottom,self.front,self.top
    def print_top(self): print(self.top)

label = list(input().split())
order_list = list(input())
d = dice(label)
for order in order_list:
    d.roll(order)
d.print_top()