class dice():
    def __init__(self,number):
        self.number = number

    def korokoro(self,com):
        if com == 'E':
            self.number = [self.number[i] for i in [3,1,0,5,4,2]]
        if com == 'S':
            self.number = [self.number[i] for i in [4,0,2,3,5,1]]
        if com == 'N':
            self.number = [self.number[i] for i in [1,5,2,3,0,4]]
        if com == 'W':
            self.number = [self.number[i] for i in [2,1,5,0,4,3]]
i_number = [int(x) for x in input().split()]
com_list = input()
d = dice(i_number)
for c in com_list:
    d.korokoro(c)
print(d.number[0])

