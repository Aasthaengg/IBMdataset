#!usr/bin/env python3

import sys


class Die:
    def __init__(self, pips):
        self.pips = pips

    def move_die(self, direction):
        tmp = int()
        if direction == 'N':
            tmp = self.pips[0]
            self.pips[0] = self.pips[1]
            self.pips[1] = self.pips[5]
            self.pips[5] = self.pips[4]
            self.pips[4] = tmp
            del tmp
        elif direction == 'S':
            tmp = self.pips[0]
            self.pips[0] = self.pips[4]
            self.pips[4] = self.pips[5]
            self.pips[5] = self.pips[1]
            self.pips[1] = tmp
            del tmp
        elif direction == 'E':
            tmp = self.pips[0]
            self.pips[0] = self.pips[3]
            self.pips[3] = self.pips[5]
            self.pips[5] = self.pips[2]
            self.pips[2] = tmp
            del tmp
        elif direction == 'W':
            tmp = self.pips[0]
            self.pips[0] = self.pips[2]
            self.pips[2] = self.pips[5]
            self.pips[5] = self.pips[3]
            self.pips[3] = tmp
            del tmp

    def spin_die_clockwise(self):
        tmp = self.pips[1]
        self.pips[1] = self.pips[2]
        self.pips[2] = self.pips[4]
        self.pips[4] = self.pips[3]
        self.pips[3] = tmp
        del tmp

    def get_upside(self):
        return self.pips[0]

    def get_frontside(self):
        return self.pips[1]

    def get_rightside(self):
        return self.pips[2]


def init_die():
    pips = [int(pip) for pip in sys.stdin.readline().strip('\n').split()]
    die = Die(pips)
    return die


def roll_die(die):
    directions = list(sys.stdin.readline().strip('\n'))

    for direction in directions:
        die.move_die(direction)

    return die


def main():
    die = init_die()
    q = int(sys.stdin.readline().strip('\n'))

    for question in range(q):
        q_pips = [int(pip) for pip in sys.stdin.readline().strip('\n').split()]

        if q_pips[0] == die.pips[0]:
            pass
        elif q_pips[0] == die.pips[1]:
            die.move_die('N')
        elif q_pips[0] == die.pips[2]:
            die.move_die('W')
        elif q_pips[0] == die.pips[3]:
            die.move_die('E')
        elif q_pips[0] == die.pips[4]:
            die.move_die('S')
        elif q_pips[0] == die.pips[5]:
            die.move_die('N')
            die.move_die('N')

        while die.get_frontside() != q_pips[1]:
            die.spin_die_clockwise()

        print(die.get_rightside())


if __name__ == '__main__':
    main()