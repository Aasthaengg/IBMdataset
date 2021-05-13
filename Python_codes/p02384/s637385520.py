class Dice:
    __slots__ = ['n_list', 'pair_list']

    def __init__(self, n_tup):
        self.n_list = list(n_tup)
        self.pair_list = [self.return_dice_round_pair(self.n_list, 2, 3, 5, 4),
                          self.return_dice_round_pair(self.n_list, 1, 4, 6, 3),
                          self.return_dice_round_pair(self.n_list, 1, 2, 6, 5),
                          self.return_dice_round_pair(self.n_list, 1, 5, 6, 2),
                          self.return_dice_round_pair(self.n_list, 1, 3, 6, 4),
                          self.return_dice_round_pair(self.n_list, 2, 4, 5, 3)
                          ]

    @staticmethod
    def roll_switch(n_list, from_idx_list, to_idx_list):
        n_list[from_idx_list[0] - 1], \
        n_list[from_idx_list[1] - 1], \
        n_list[from_idx_list[2] - 1], \
        n_list[from_idx_list[3] - 1] \
            = n_list[to_idx_list[0] - 1], \
              n_list[to_idx_list[1] - 1], \
              n_list[to_idx_list[2] - 1], \
              n_list[to_idx_list[3] - 1]
        return n_list

    def roll(self, direction):
        if direction == "N":
            self.n_list = self.roll_switch(self.n_list, [1, 2, 6, 5], [2, 6, 5, 1])

        elif direction == "E":
            self.n_list = self.roll_switch(self.n_list, [1, 3, 6, 4], [4, 1, 3, 6])

        if direction == "S":
            self.n_list = self.roll_switch(self.n_list, [1, 2, 6, 5], [5, 1, 2, 6])

        if direction == "W":
            self.n_list = self.roll_switch(self.n_list, [1, 3, 6, 4], [3, 6, 4, 1])

    @staticmethod
    def return_dice_round_pair(n_list, a, b, c, d):
        return [(n_list[a-1], n_list[b-1]),
                (n_list[b-1], n_list[c-1]),
                (n_list[c-1], n_list[d-1]),
                (n_list[d-1], n_list[a-1])]

    def return_right_num(self, top, forward):
        for i in range(6):
            if (top, forward) in self.pair_list[i]:
                return self.n_list[i]


dice = Dice([int(x) for x in input().split()])
cmd_cnt = int(input())

for i in range(cmd_cnt):
    top, forward = (int(x) for x in input().split())
    print(dice.return_right_num(top, forward))