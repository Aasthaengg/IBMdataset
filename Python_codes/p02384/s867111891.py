
#0:上面　1:S 2:E 3:W 4:N 5:下
class Dice:
    def __init__(self):#クラス内で用いる変数の定義（クラス作成時に代入しなくてよい）
        self.number = [i for i in range(6)]
        self.work = [i for i in range(6)]
        self.order = 'NNNNWNNNWNNNENNNENNNWNNN'
    #サイコロの目の数を設定
    def setNumber(self, n0, n1, n2, n3, n4, n5):
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5
        
    #サイコロを転がせ，それぞれのいちを追跡
    def roll(self, loc):#loc:
    #初期位置
        for i in range(6):
            self.work[i] = self.number[i]
        if loc == 'E':
            self.setNumber(self.work[3],self.work[1],self.work[0],self.work[5],self.work[4],self.work[2])
        elif loc == 'N':
            self.setNumber(self.work[1],self.work[5],self.work[2],self.work[3],self.work[0],self.work[4])
        elif loc == 'S':
            self.setNumber(self.work[4],self.work[0],self.work[2],self.work[3],self.work[5],self.work[1])
        else:
            self.setNumber(self.work[2],self.work[1],self.work[5],self.work[0],self.work[4],self.work[3])
    
    def query(self, top_num, front_num):
        self.save_data = [i for i in range(6)]
        #元のデータの保存
        for i in range(len(self.number)):
            self.save_data[i] = self.number[i]
        
        ret = -1
        
        for i in range(len(self.order)):
            self.roll(self.order[i])
            if self.number[0] == top_num and self.number[1] == front_num:
                ret = self.number[2]
                break
        return ret;
    

dice = Dice()
table = list(map(int, input().split()))
dice.setNumber(table[0],table[1],table[2],table[3],table[4],table[5])#init
# loc_array=str(input())

q = int(input())
for loop in range(q):
    u, f = map(int, input().split())
    print(dice.query(u, f))

# for tmp_loc in loc_array:
    # dice.roll(tmp_loc)
# print(dice.get_Top())
        
        
        
