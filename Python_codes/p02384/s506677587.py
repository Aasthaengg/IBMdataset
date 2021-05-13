class Dice():
    def __init__(self):
        self.num = [0 for _ in range(6)]
    
    def set_num(self, n0, n1, n2, n3, n4, n5):
        self.num[0] = n0
        self.num[1] = n1
        self.num[2] = n2
        self.num[3] = n3
        self.num[4] = n4
        self.num[5] = n5
    
    def roll(self, order):
        tmp = self.num.copy()
        
        if order == "N":
            self.set_num(tmp[1], tmp[5], tmp[2], tmp[3], tmp[0], tmp[4])
        elif order == "S":
            self.set_num(tmp[4], tmp[0], tmp[2], tmp[3], tmp[5], tmp[1])
        elif order == "E":
            self.set_num(tmp[3], tmp[1], tmp[0], tmp[5], tmp[4], tmp[2])
        elif order == "W":
            self.set_num(tmp[2], tmp[1], tmp[5], tmp[0], tmp[4], tmp[3])
        elif order == "rot_Clock":
            self.set_num(tmp[0], tmp[2], tmp[4], tmp[1], tmp[3], tmp[5])
        else:
            print("Error: 不正な入力です")

    def get_top_num(self):
        return self.num[0]
        
    
# Input)()
init_num = [int(_) for _ in input().split()]
n_question = int(input())

# Main 
dice = Dice()
dice.set_num(init_num[0], init_num[1], init_num[2], init_num[3], init_num[4], init_num[5])


for i in range(n_question):
    n_top, n_front = map(int, input().split())
    index_n_top = dice.num.index(n_top)
    index_n_front = dice.num.index(n_front)
    
    # print(f"(Init{i}) n_top: {n_top}, n_front: {n_front}")
    # print(f"(Init{i}) dice: {dice.num}")
    # print(f"(Init{i}) index_n_top: {index_n_top}, index_n_front: {index_n_front}")
    # print()
    
    while index_n_top != 0:
        if index_n_top in [0, 1, 4, 5]:
            dice.roll("N")
            index_n_top = dice.num.index(n_top)
            index_n_front = dice.num.index(n_front)
            # print("roll N")
            # print(f"-> index_n_top: {index_n_top}, index_n_front: {index_n_front}")
        else:
            dice.roll("E")
            index_n_top = dice.num.index(n_top)
            index_n_front = dice.num.index(n_front)
            # print("roll E")
            # print(f"-> index_n_top: {index_n_top}, index_n_front: {index_n_front}")
            
    while index_n_front != 1:
            dice.roll("rot_Clock")
            index_n_top = dice.num.index(n_top)
            index_n_front = dice.num.index(n_front)
            # print("roll C")
            # print(f"-> index_n_top: {index_n_top}, index_n_front: {index_n_front}")                
                
    print(dice.num[2])
