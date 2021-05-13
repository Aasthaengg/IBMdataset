mask = [[i for i in range(6)], (1, 5, 2, 3, 0, 4), (2, 1, 5, 0, 4,3),(3, 1, 0, 5, 4, 2), (4, 0, 2, 3, 5, 1)]
mask += [[mask[1][i] for i in mask[1]]]

TOP, FRONT, RIGHT, LEFT, BACK, BOTTOM = mask[0]

def set_top(dice, top):
    return [dice[i] for i in mask[top]]

def set_front(dice, front):
    twist = (0, 3, 1, 4, 2, 5)
    while dice[FRONT] != front:
        dice = [dice[i] for i in twist]
    return dice
        
label = input().split()
q = int(input())
for _ in range(q):
    top, front = map(label.index, input().split())
    dice = set_top(mask[0], top)
    dice = set_front(dice, front)
    print(label[dice[RIGHT]])