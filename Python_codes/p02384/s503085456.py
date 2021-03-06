class Dice:
    def __init__(self,l1,l2,l3,l4,l5,l6):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.l5 = l5
        self.l6 = l6
        self.top = 1
        self.front = 2
        self.right = 3

    def get_up_front(self):
        return eval("("+"self." + 'l' + str(self.top)+","+"self." + 'l' + str(self.front)+")")

    def get_right(self):
        return eval("self." + 'l' + str(self.right))

    def rot(self):
        self.front,self.right = self.right,7-self.front

    def move(self, order):
        if order == 'S':
            pretop = self.top
            self.top = 7 - self.front
            self.front = pretop
        elif order == 'E':
            pretop = self.top
            self.top = 7 - self.right
            self.right = pretop
        elif order == 'N':
            pretop = self.top
            self.top = self.front
            self.front = 7 - pretop
        elif order == 'W':
            pretop = self.top
            self.top = self.right
            self.right = 7 - pretop

l = list(map(int,input().split()))
q = int(input())
d = Dice(l[0],l[1],l[2],l[3],l[4],l[5])

for i in range(q):
    up,front = list(map(int,input().split()))
    while (up,front) != d.get_up_front():
        for j in range(4):
            d.move('S')
            if up == d.get_up_front()[0]:
                break
        if up != d.get_up_front()[0]:
            for l in range(4):
                d.move('E')
                if up == d.get_up_front()[0]:
                    break
        for k in range(4):
            d.rot()
            if front == d.get_up_front()[1]:
                break
    print (d.get_right())