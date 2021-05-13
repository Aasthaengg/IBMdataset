#サイコロの問題B
class Dice:
    def __init__(self, input_dice):
        self.flow = [input_dice[3], input_dice[1], input_dice[0], input_dice[5], input_dice[2], input_dice[4]]
        self.dice = [input_dice[3], input_dice[1], input_dice[0], input_dice[5], input_dice[2], input_dice[4]]
  
    def setNumber(self, n0, n1, n2, n3, n4, n5):
        self.dice[0] = n0
        self.dice[1] = n1
        self.dice[2] = n2
        self.dice[3] = n3
        self.dice[4] = n4
        self.dice[5] = n5
        return self.dice
    
    def roll(self, dir):
        if dir == 'S':
            self.setNumber(self.flow[0], self.flow[2], self.flow[5], self.flow[1], self.flow[4], self.flow[3])
            self.flow = self.dice
            return self.dice
        if dir == 'N':
            self.setNumber(self.flow[0], self.flow[3], self.flow[1], self.flow[5], self.flow[4], self.flow[2])
            self.flow = self.dice
            return self.dice
        if dir == 'W':
            self.setNumber(self.flow[2], self.flow[1], self.flow[4], self.flow[0], self.flow[3], self.flow[5])
            self.flow = self.dice
            return self.dice
        if dir == 'E':
            self.setNumber(self.flow[3], self.flow[1], self.flow[0], self.flow[4], self.flow[2], self.flow[5])
            self.flow = self.dice
            return self.dice

    def right_side(self, ue, mae):
        #以下メモ書き[1,2,3,4,5,6]の入力が与えられたとする
        #以下南北方向を軸に回転させる
        #最初2が前面
        i = 0
        for i in range(4):
            self.roll('W')
            if self.dice[2] == ue and self.dice[1] == mae:
                print(self.dice[4])
                break
        #1を前面に持ってきて回転させる
        self.roll('S')
        for i in range(4):
            self.roll('W')
            if self.dice[2] == ue and self.dice[1] == mae:
                print(self.dice[4])
                break
        #5を前面に持ってきて回転させる
        self.roll('S')
        for i in range(4):
            self.roll('W')
            if self.dice[2] == ue and self.dice[1] == mae:
                print(self.dice[4])
                break
        #6を前面に持ってきて回転させる
        self.roll('S')
        for i in range(4):
            self.roll('W')
            if self.dice[2] == ue and self.dice[1] == mae:
                print(self.dice[4])
                break
        #4を前面に持ってきて回転させる
        self.roll('E')
        self.roll('S')
        for i in range(4):
            self.roll('W')
            if self.dice[2] == ue and self.dice[1] == mae:
                print(self.dice[4])
                break
        #3を前面に持ってきて回転させる
        self.roll('N')
        self.roll('N')
        for i in range(4):
            self.roll('W')
            if self.dice[2] == ue and self.dice[1] == mae:
                print(self.dice[4])
                break

dice = list(map(int, input().split()))
n = int(input())
ue = [0]*n
mae = [0]*n
for i in range(n):
    ue[i], mae[i] = map(int, input().split())

d = Dice(dice)
for i in range(n):
    d.right_side(ue[i], mae[i])
