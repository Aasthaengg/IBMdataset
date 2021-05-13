class dice:
    def __init__(self, f0, f1, f2, f3, f4, f5):
        self.dice_num = [f0, f1, f2, f3, f4, f5]

    def roll_dice(self, command):
        for i in command:
            if i == 'N':
                tmp = self.dice_num[0]
                self.dice_num[0] = self.dice_num[1]
                self.dice_num[1] = self.dice_num[5]
                self.dice_num[5] = self.dice_num[4]
                self.dice_num[4] = tmp

            if i == 'S':
                tmp = self.dice_num[0]
                self.dice_num[0] = self.dice_num[4]
                self.dice_num[4] = self.dice_num[5]
                self.dice_num[5] = self.dice_num[1]
                self.dice_num[1] = tmp

            if i == 'E':
                tmp = self.dice_num[0]
                self.dice_num[0] = self.dice_num[3]
                self.dice_num[3] = self.dice_num[5]
                self.dice_num[5] = self.dice_num[2]
                self.dice_num[2] = tmp

            if i == 'W':
                tmp = self.dice_num[0]
                self.dice_num[0] = self.dice_num[2]
                self.dice_num[2] = self.dice_num[5]
                self.dice_num[5] = self.dice_num[3]
                self.dice_num[3] = tmp

    def print_topface(self):
        print(self.dice_num[0])


if __name__ == "__main__":
    num_list = list(map(int, input().split()))
    command_str = input()
    mydice = dice(*num_list)
    mydice.roll_dice(command_str)
    mydice.print_topface()

