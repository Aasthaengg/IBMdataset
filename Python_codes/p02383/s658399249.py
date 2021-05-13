class Dice:
    def __init__(self, top, south, east, west, north, bottom):
        self.eyes = [top, south, east, west, north, bottom]


def roll_to_S(dice):
    eyes = dice.eyes

    return Dice(eyes[4], eyes[0], eyes[2], eyes[3], eyes[5], eyes[1])


def roll_to_N(dice):
    eyes = dice.eyes

    return Dice(eyes[1], eyes[5], eyes[2], eyes[3], eyes[0], eyes[4])


def roll_to_W(dice):
    eyes = dice.eyes

    return Dice(eyes[2], eyes[1], eyes[5], eyes[0], eyes[4], eyes[3])


def roll_to_E(dice):
    eyes = dice.eyes

    return Dice(eyes[3], eyes[1], eyes[0], eyes[5], eyes[4], eyes[2])


if __name__ == "__main__":
    eyes = list(map(int, input().split()))

    roll_directions = input()

    dice = Dice(*eyes)

    roll_function_table = {
        "S": roll_to_S,
        "N": roll_to_N,
        "W": roll_to_W,
        "E": roll_to_E
    }

    for roll_direction in roll_directions:
        dice = roll_function_table[roll_direction](dice)

    print(dice.eyes[0])


