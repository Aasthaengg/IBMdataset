class dice():
    def __init__(self):
        self.number = [i for i in range(6)]
        self.work = [i for i in range(6)]
    
    def setnum(self,s):
        self.number = s

    def kai(self,h):
        tmp = self.number
        if h == 'E':
            self.number = [tmp[3],tmp[1],tmp[0],tmp[5],tmp[4],tmp[2]]
        elif h == 'S':
            self.number = [tmp[4],tmp[0],tmp[2],tmp[3],tmp[5],tmp[1]]
        elif h == 'W':
            self.number = [tmp[2],tmp[1],tmp[5],tmp[0],tmp[4],tmp[3]]
        elif h == 'N':
            self.number = [tmp[1],tmp[5],tmp[2],tmp[3],tmp[0],tmp[4]]

    def Qright(self,up,flont,num):
        uf = (up,flont)
        if uf == (num[1],num[2]) or uf ==(num[2],num[4]) or uf ==(num[4],num[3]) or uf ==(num[3],num[1]):
            ans = num[0]
        elif uf == (num[0],num[3]) or uf ==(num[3],num[5]) or uf ==(num[5],num[2]) or uf ==(num[2],num[0]):
            ans = num[1]
        elif uf == (num[0],num[1]) or uf ==(num[1],num[5]) or uf ==(num[5],num[4]) or uf ==(num[4],num[0]):
            ans = num[2]
        elif uf == (num[0],num[4]) or uf ==(num[4],num[5]) or uf ==(num[5],num[1]) or uf ==(num[1],num[0]):
            ans = num[3]
        elif uf == (num[0],num[2]) or uf ==(num[2],num[5]) or uf ==(num[5],num[3]) or uf ==(num[3],num[0]):
            ans = num[4]
        elif uf == (num[1],num[3]) or uf ==(num[3],num[4]) or uf ==(num[4],num[2]) or uf ==(num[2],num[1]):
            ans = num[5]
        print(ans)


num = list(map(int,input().split()))
#kaitenn = input()
q = int(input())
dice = dice()
dice.setnum(num)
for i in range(q):
    up,flont = map(int,input().split())
    dice.Qright(up,flont,num)
#print(dice.number[0])
