class Dice(object):
    """Dice Class

    """

    def __init__(self, numbers):
        """

        Args:
            numbers:
        """
        self.numbers_inverse = {numbers[0]: 1, numbers[1]: 2, numbers[2]: 3, numbers[3]: 4, numbers[4]: 5,
                                numbers[5]: 6}
        self.numbers = {1: numbers[0], 2: numbers[1], 3: numbers[2], 4: numbers[3], 5: numbers[4], 6: numbers[5]}

        self.vertical = [self.numbers[1], self.numbers[2], self.numbers[6], self.numbers[5]]
        self.horizontal = [self.numbers[4], self.numbers[1], self.numbers[3], self.numbers[6]]

    def move_dice(self, s):
        """

        Args:
            s: move direction

        Returns:

        """
        if s == 'N':
            self.move_north()
        elif s == 'S':
            self.move_south()
        elif s == 'W':
            self.move_west()
        elif s == 'E':
            self.move_east()

    def move_south(self):
        """move this dice towered north
        """
        self.vertical = (self.vertical * 2)[3:7]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]

    def move_north(self):
        """move this dice towered south
        """
        self.vertical = (self.vertical * 2)[1:5]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]

    def move_east(self):
        """move this dice towered east
        """
        self.horizontal = (self.horizontal * 2)[3:7]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]

    def move_west(self):
        """move this dice towered west
        """
        self.horizontal = (self.horizontal * 2)[1:5]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]

    def get_top(self):
        return self.vertical[0]


dice = Dice([int(x) for x in raw_input().split()])
number_of_questions = int(raw_input())
counter = 0
while counter < number_of_questions:
    [top, front] = [int(x) for x in raw_input().split()]
    decision_list = "".join([str(x) for x in [dice.numbers_inverse[top], dice.numbers_inverse[front]]])
    if decision_list in "1265" * 2:
        print(dice.numbers[3])
    elif decision_list in "5621" * 2:
        print(dice.numbers[4])
    elif decision_list in "4235" * 2:
        print(dice.numbers[1])
    elif decision_list in "5324" * 2:
        print(dice.numbers[6])
    elif decision_list in "1364" * 2:
        print(dice.numbers[5])
    elif decision_list in "4631" * 2:
        print(dice.numbers[2])
    else:
        print("aho")
    counter += 1