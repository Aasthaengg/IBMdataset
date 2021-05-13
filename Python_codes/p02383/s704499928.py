class Dice:
    def __init__(self,tb):
        self.table = tb
    def spin(self, dirc):
        directions = dirc
        table1 = self.table
        
        for direction in directions:
            res = [0]*6
            if direction == "N":
                #[1,2,4,8,16,32]
                #[2,32,4,8,1,16]
                res[0] = table1[1]
                res[1] = table1[5]
                res[2] = table1[2]
                res[3] = table1[3]
                res[4] = table1[0]
                res[5] = table1[4]
                
            elif direction == "S":
                #[1,2,4,8,16,32]
                #[16,1,4,8,32,2]
                res[0] = table1[4]
                res[1] = table1[0]
                res[2] = table1[2]
                res[3] = table1[3]
                res[4] = table1[5]
                res[5] = table1[1]
                
            elif direction == "E":
                #[1,2,4,8,16,32]
                #[8,2,1,32,16,4]
                res[0] = table1[3]
                res[1] = table1[1]
                res[2] = table1[0]
                res[3] = table1[5]
                res[4] = table1[4]
                res[5] = table1[2]

            elif direction == "W":
                res[0] = table1[2]
                res[1] = table1[1]
                res[2] = table1[5]
                res[3] = table1[0]
                res[4] = table1[4]
                res[5] = table1[3]
            
            table1 =  res
        self.table = table1
tb1 = list(map(int,input().split()))
directions = input()


dice1 = Dice(tb1)
dice1.spin(directions)
print(dice1.table[0])
