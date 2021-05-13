class Dice:
    def __init__(self, lst):
        self.a = lst[0]
        self.b = lst[1]
        self.c = lst[2]
        self.d = lst[3]
        self.e = lst[4]
        self.f = lst[5]
        
    def roll(self, orders):
        for order in orders:
            if order=='W':
                tmp = self.a
                self.a = self.c
                self.c = self.f
                self.f = self.d
                self.d = tmp
            elif order=='E':
                tmp = self.a
                self.a = self.d
                self.d = self.f
                self.f = self.c
                self.c = tmp
            elif order=='S':
                tmp = self.a
                self.a = self.e
                self.e = self.f
                self.f = self.b
                self.b = tmp
            elif order=='N':
                tmp = self.a
                self.a = self.b
                self.b = self.f
                self.f = self.e
                self.e = tmp
#             print(self.a, self.b, self.c, self.d, self.e, self.f)
#         print(self.a)
       
            
import random
if __name__ == '__main__':
    lst = [int(x) for x in input().split()]
    q = int(input())
    questions = [[int(x) for x in input().split()] for _ in range(q)]
    
    dice = Dice(lst)    # 初期化
    direction = ['N', 'E', 'S', 'W']
    for question in questions:
        """ diceをランダムに回し、所望の状態になったら状態を出力
        """
        while True:
            dice.roll(random.choice(direction))
            if dice.a==question[0] and dice.b==question[1]:
                print(dice.c)
                break
