dice = list(map(int, input().split()))
mask = {
    'N': (1, 5, 2, 3, 0, 4),
    'R': (0, 2, 4, 1, 3, 5)
    }


for i in range(int(input())):
    a, b = map(int, input().split())

    lim = 0
    while dice[0] != a:
        dice = [dice[x] for x in mask['N']]
        lim += 1
        if lim == 4:
            dice = [dice[x] for x in mask['R']]
            lim = 0
    while dice[1] != b:
        dice = [dice[x] for x in mask['R']]
    print(dice[2])

