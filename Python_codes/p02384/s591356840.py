class Dice:
    rmap = [[2,3,5,4,2],
            [1,4,6,3,1],
            [1,2,6,5,1],
            [5,6,2,1,5],
            [3,6,4,1,3],
            [4,5,3,2,4] ]

    def __init__(self,list):
        self.num = list

    def lookup_right_side(self,u,s):
        index_upside = self.num.index(u)
        map_arr = self.rmap[index_upside]
        map_arr_dice_val = [ self.num[i-1] for i in map_arr ]
        index_next_map = map_arr_dice_val.index(s) + 1
        index_rightside = map_arr[index_next_map]
        return self.num[index_rightside-1]

spots = map(int,raw_input().split())
n = input()
questions = [ map(int,raw_input().split()) for _ in range(n) ]

dice = Dice(spots)
for i in questions:
    print dice.lookup_right_side(i[0],i[1])