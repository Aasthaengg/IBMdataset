class dice_2:
    def __init__(self,label):
        self.spots = label

    def result(self,top,front):
        if self.spots.index(top)+1 == 1:
            self.order=[2,3,5,4,2]
        elif self.spots.index(top)+1 == 2:
            self.order=[6,3,1,4,6]
        elif self.spots.index(top)+1 == 3:
            self.order=[2,6,5,1,2]
        elif self.spots.index(top)+1 == 4:
            self.order=[2,1,5,6,2]
        elif self.spots.index(top)+1 == 5:
            self.order=[1,3,6,4,1]
        elif self.spots.index(top)+1 == 6:
            self.order=[2,4,5,3,2]

        for i in range(4):
            if self.order[i] == self.spots.index(front)+1:
                self.right = self.order[i+1]

    def output(self):
        print(self.spots[self.right-1])

label = list(map(int,input().split()))
dice = dice_2(label)
for i in range(int(input())):
    top,front = map(int,(input().split()))
    dice.result(top,front)
    dice.output()