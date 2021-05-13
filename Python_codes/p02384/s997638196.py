class Dice(object):
    def __init__(self, numbers: list):
        self.numbers = dict(zip(("T", "S", "E", "W", "N", "B"), numbers))

    def _roll(self, old_part: tuple):
        new_part = old_part[1:] + (old_part[0],)
        new_numbers = [self.numbers[face] for face in new_part]

        for old, new in zip(old_part, new_numbers):
            self.numbers[old] = new

    def vroll(self, reverse=False):
        """北方向に回転"""
        old_part = ("N", "T", "S", "B")
        self._roll(old_part if not reverse else old_part[::-1])

    def hroll(self, reverse=False):
        """時計回りに回転"""
        old_part = ("N", "W", "S", "E")
        self._roll(old_part if not reverse else old_part[::-1])

    def roll_to(self, direction: str):

        if direction == "N":
            self.vroll()
        elif direction == "S":
            self.vroll(reverse=True)
        elif direction == "E":
            self.hroll(reverse=True)
            self.vroll()
            self.hroll()
        elif direction == "W":
            self.hroll()
            self.vroll()
            self.hroll(reverse=True)
        else:
            raise AssertionError

    def set_pos(self, top, front):
        numbers = self.numbers
        if top in (numbers["E"], numbers["W"]):
            self.hroll()
        while top != numbers["T"]:
            self.vroll()
        while front != numbers["S"]:
            self.hroll()


numbers = list(map(int, input().split()))
dice = Dice(numbers)

outs = []
for _ in range(int(input())):
    top, front = map(int, input().split())
    dice.set_pos(top, front)
    outs.append(dice.numbers["E"])

print(*outs, sep="\n")

