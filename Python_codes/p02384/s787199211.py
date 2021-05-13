# Dice I

d = [int(i) for i in input().rstrip().split()]

class Dice:
    def __init__(self, a1, a2, a3, a4, a5, a6):
        # サイコロを縦横にたどると書いてある数字(index1は真上、index3は真下の数字)
        self.face = [a1, a2, a3, a4, a5, a6]
        self.v = [a5, a1, a2, a6] # 縦方向
        self.h = [a4, a1, a3, a6] # 横方向
        self.det = 1
        # print(self.v, self.h)

    # サイコロの上面の数字を表示
    def top(self):
        return self.v[1]

    # サイコロを北方向に倒す
    def north(self):
        newV = [self.v[1], self.v[2], self.v[3], self.v[0]]
        self.v = newV
        self.h[1] = self.v[1]
        self.h[3] = self.v[3]
        return self.v, self.h

    # サイコロを南方向に倒す
    def south(self):
        newV = [self.v[3], self.v[0], self.v[1], self.v[2]]
        self.v = newV
        self.h[1] = self.v[1]
        self.h[3] = self.v[3]
        return self.v, self.h

    # サイコロを東方向に倒す
    def east(self):
        newH = [self.h[3], self.h[0], self.h[1], self.h[2]]
        self.h = newH
        self.v[1] = self.h[1]
        self.v[3] = self.h[3]
        return self.v, self.h

    # サイコロを西方向に倒す
    def west(self):
        newH = [self.h[1], self.h[2], self.h[3], self.h[0]]
        self.h = newH
        self.v[1] = self.h[1]
        self.v[3] = self.h[3]
        return self.v, self.h

    def searchFace(self, a):
        b = 0
        for i in range(6):
            if a == self.face[i]:
                # print('一致しました')
                b = i + 1
        return b

    def smallen(self, x): # a は 1 から 6 のどれか
        y = int(7 / 2 - abs(x - 7 / 2))
        if x != y:
            self.det *= -1
        # print(self.det)
        return y

    def rightSide(self, top, front):
        r = 0
        if top == 1 and front == 2:
            r = 3
        elif top == 2 and front == 3:
            r = 1
        elif top == 3 and front == 1:
            r = 2
        elif top == 1 and front == 3:
            r = 5
        elif top == 3 and front == 2:
            r = 6
        elif top == 2 and front == 1:
            r = 4
        if self.det == -1:
            r = 7 - r
        return r

dice1 = Dice(d[0], d[1], d[2], d[3], d[4], d[5])

# command = list(input().rstrip())
# print(command)

# for i, a in enumerate(command):
#     if a == 'N':
#         dice1.north()
#     elif a == 'S':
#         dice1.south()
#     elif a == 'E':
#         dice1.east()
#     elif a == 'W':
#         dice1.west()
# print(dice1.top())

questionAmount = int(input())
for i in range(questionAmount):
    # Initialize det
    dice1.det = 1
    question = [int(i) for i in input().rstrip().split()]
    a = dice1.searchFace(question[0])
    b = dice1.searchFace(question[1])
    # print(a, b)
    top = dice1.smallen(a)
    front = dice1.smallen(b)
    # print(top, front)
    position = dice1.rightSide(top, front)
    answer = dice1.face[position - 1]
    print(answer)

