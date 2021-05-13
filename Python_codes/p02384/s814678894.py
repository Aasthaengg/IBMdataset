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

    def roll_dice(self, str):
        """

        Args:
            str: move direction

        Returns:

        """
        for s in str:
            if s == 'N':
                self.move_north()
            elif s == 'S':
                self.move_south()
            elif s == 'W':
                self.move_west()
            elif s == 'E':
                self.move_east()

    def set_top(self, value):
        """
        Args:
            value: target_value
        """
        counter = 0
        while counter < 4:
            if self.vertical[0] == value:
                self.map_values()
                return
            else:
                self.roll_dice("S")
            counter += 1
        counter = 0
        while counter < 4:
            if self.vertical[0] == value:
                self.map_values()
                return
            else:
                self.roll_dice("W")
            counter += 1

    def set_front(self, value):
        """
        Args:
            value: target value
        """
        counter = 0
        while counter < 4:
            if self.vertical[1] == value:
                self.map_values()
                return
            else:
                self.roll_dice("SWN")
            counter += 1

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

    def map_values(self):
        self.numbers[1] = self.vertical[0]
        self.numbers[2] = self.vertical[1]
        self.numbers[3] = self.horizontal[2]
        self.numbers[4] = self.horizontal[0]
        self.numbers[5] = self.horizontal[3]
        self.numbers[6] = self.vertical[3]

    def get_top(self):
        return self.vertical[0]


dice = Dice([int(x) for x in raw_input().split()])
number_of_questions = int(raw_input())
counter = 0
while counter < number_of_questions:
    [top, front] = [int(x) for x in raw_input().split()]
    dice.set_top(top)
    dice.set_front(front)
    print(dice.numbers[3])

    counter += 1