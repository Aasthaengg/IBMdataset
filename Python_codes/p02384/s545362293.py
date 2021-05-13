class Dice:
    def __init__(self, e1, e2, e3, e4, e5, e6):
        self.eye1 = e1
        self.eye2 = e2
        self.eye3 = e3
        self.eye4 = e4
        self.eye5 = e5
        self.eye6 = e6
    
    def roll_e(self):
        tmp_eye   = self.eye3
        self.eye3 = self.eye1
        self.eye1 = self.eye4
        self.eye4 = self.eye6
        self.eye6 = tmp_eye
    
    def roll_n(self):
        tmp_eye   = self.eye5
        self.eye5 = self.eye1
        self.eye1 = self.eye2
        self.eye2 = self.eye6
        self.eye6 = tmp_eye
    
    def roll_s(self):
        tmp_eye   = self.eye2
        self.eye2 = self.eye1
        self.eye1 = self.eye5
        self.eye5 = self.eye6
        self.eye6 = tmp_eye
    
    def roll_w(self):
        tmp_eye   = self.eye4
        self.eye4 = self.eye1
        self.eye1 = self.eye3
        self.eye3 = self.eye6
        self.eye6 = tmp_eye
    
    def roll_h(self):
        tmp_eye   = self.eye2
        self.eye2 = self.eye3
        self.eye3 = self.eye5
        self.eye5 = self.eye4
        self.eye4 = tmp_eye
    
    def get_eye1(self):
        return self.eye1
    
    def get_eye2(self):
        return self.eye2

    def get_eye3(self):
        return self.eye3

e1, e2, e3, e4 ,e5, e6 = map(int,input().split())
dice1 = Dice(e1, e2, e3, e4 ,e5, e6)
roll = int(input())
for i in range(roll):
    t1, t2 = map(int,input().split())
    while t1 != dice1.get_eye1():
        dice1.roll_e()
        if t1 != dice1.get_eye1():
            dice1.roll_n()
        else:
            break
    while t2 != dice1.get_eye2():
        dice1.roll_h()
    print(dice1.get_eye3())
