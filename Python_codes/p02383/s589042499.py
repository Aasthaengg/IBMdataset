# -*- coding:utf-8 -*-


class Dice(object):
    def __init__(self, one, two, thr, fou, fiv, six):
        self._one = one
        self._two = two
        self._thr = thr
        self._fou = fou
        self._fiv = fiv
        self._six = six

    def roll(self, direction):
        if direction == "W":
            dice = self._roll_west()
        elif direction == "N":
            dice = self._roll_noth()
        elif direction == "E":
            dice = self._roll_east()
        elif direction == "S":
            dice = self._roll_south()
        else:
            raise ValueError

        return dice

    def _roll_west(self):
        return Dice(self._thr, self._two, self._six,
                    self._one, self._fiv, self._fou)

    def _roll_noth(self):
        return Dice(self._two, self._six, self._thr,
                    self._fou, self._one, self._fiv)

    def _roll_east(self):
        return Dice(self._fou, self._two, self._one,
                    self._six, self._fiv, self._thr)

    def _roll_south(self):
        return Dice(self._fiv, self._one, self._thr,
                    self._fou, self._six, self._two)

    def get_sides(self):
        return [self._one, self._two, self._thr,
                self._fou, self._fiv, self._six]


if __name__ == "__main__":
    args = [int(n) for n in input().split()]
    dice = Dice(*args)
    for dire in input():
        dice = dice.roll(dire)

    print(dice.get_sides()[0])
