class Dice():
    def __init__(self, l):
        self.value = l
    def roll(self,s):
        new_list = [0]*6
        if s == "W":
            new_list[0] = self.value[2]
            new_list[1] = self.value[1]
            new_list[2] = self.value[5]
            new_list[3] = self.value[0]
            new_list[4] = self.value[4]
            new_list[5] = self.value[3]
        if s == "E":
            new_list[0] = self.value[3]
            new_list[1] = self.value[1]
            new_list[2] = self.value[0]
            new_list[3] = self.value[5]
            new_list[4] = self.value[4]
            new_list[5] = self.value[2]
        if s == "N":
            new_list[0] = self.value[1]
            new_list[1] = self.value[5]
            new_list[2] = self.value[2]
            new_list[3] = self.value[3]
            new_list[4] = self.value[0]
            new_list[5] = self.value[4]
        if s == "S":
            new_list[0] = self.value[4]
            new_list[1] = self.value[0]
            new_list[2] = self.value[2]
            new_list[3] = self.value[3]
            new_list[4] = self.value[5]
            new_list[5] = self.value[1]
        self.value = new_list

l = list(map(int,input().split()))
Dice1 = Dice(l)
n = int(input())

for i in range(n):
    one,two = map(int,input().split())
    one_index = Dice1.value.index(one)
    two_index = Dice1.value.index(two)
    if (one_index == 0 and two_index == 1) or (one_index == 1 and two_index == 5) or (one_index == 5 and two_index == 4) or (one_index == 4 and two_index == 0):
        print(Dice1.value[2])
    if (one_index == 1 and two_index == 0) or (one_index == 5 and two_index == 1) or (one_index == 4 and two_index == 5) or (one_index == 0 and two_index == 4):
        print(Dice1.value[3])
    if (one_index == 0 and two_index == 2) or (one_index == 2 and two_index == 5) or (one_index == 5 and two_index == 3) or (one_index == 3 and two_index == 0):
        print(Dice1.value[4])
    if (one_index == 2 and two_index == 0) or (one_index == 5 and two_index == 2) or (one_index == 3 and two_index == 5) or (one_index == 0 and two_index == 3):
        print(Dice1.value[1])
    if (one_index == 1 and two_index == 2) or (one_index == 2 and two_index == 4) or (one_index == 4 and two_index == 3) or (one_index == 3 and two_index == 1):
        print(Dice1.value[0])
    if (one_index == 2 and two_index == 1) or (one_index == 4 and two_index == 2) or (one_index == 3 and two_index == 4) or (one_index == 1 and two_index == 3):
        print(Dice1.value[5])
