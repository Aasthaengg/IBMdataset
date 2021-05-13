# Aizu Problem ITP_1_11_B: Dice II
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


def do_roll(dice, roll):
    d1, d2, d3, d4, d5, d6 = dice
    if roll == 'E':
        return [d4, d2, d1, d6, d5, d3]
    elif roll == 'W':
        return [d3, d2, d6, d1, d5, d4]
    elif roll == 'N':
        return [d2, d6, d3, d4, d1, d5]
    elif roll == 'S':
        return [d5, d1, d3, d4, d6, d2]
    else:
        assert False, "We should never reach this point!"
    

right_pos = {(1, 2): 3, (1, 4): 2, (1, 5): 4, (1, 3): 5,
             (2, 3): 1, (2, 1): 4, (2, 4): 6, (2, 6): 3,
             (3, 1): 2, (3, 2): 6, (3, 6): 5, (3, 5): 1,
             (4, 1): 5, (4, 2): 1, (4, 6): 2, (4, 5): 6,
             (5, 1): 3, (5, 4): 1, (5, 6): 4, (5, 3): 6,
             (6, 2): 4, (6, 3): 2, (6, 5): 3, (6, 4): 5}
def get_right(dice, top, front):
    p_top = dice.index(top) + 1
    p_front = dice.index(front)  + 1
    return dice[right_pos[(p_top, p_front)] - 1]
    """
    for k in range(4):
        dice = do_roll(dice, 'S')
        if dice[:2] == [top, front]:
            return dice[2]
    for j in range(4):
        dice = do_roll(dice, 'E')
        for k in range(4):
            dice = do_roll(dice, 'S')
            if dice[:2] == [top, front]:
                return dice[2]
    for j in range(4):
        dice = do_roll(dice, 'W')
        for k in range(4):
            dice = do_roll(dice, 'S')
            if dice[:2] == [top, front]:
                return dice[2]
    """
    
dice = [int(_) for _ in input().split()]
Q = int(input())
for q in range(Q):
    top, front = [int(_) for _ in input().split()]
    print(get_right(dice[:], top, front))