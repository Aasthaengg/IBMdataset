dice = list(map(int, input().split()))
cmd = input()

mask = {
    'N': (1, 5, 2, 3, 0, 4),
    'E': (3, 1, 0, 5, 4, 2),
    'S': (4, 0, 2, 3, 5, 1),
    'W': (2, 1, 5, 0, 4, 3)
    }

for s in cmd:
    dice = [dice[x] for x in mask[s]]

print(dice[0])

