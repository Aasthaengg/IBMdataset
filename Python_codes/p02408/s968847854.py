from sys import stdin
smap = {'S':0, 'H':1, 'C':2, 'D':3}
rsmap = 'S', 'H', 'C', 'D'

n = int(stdin.readline())

card = []
for s in range(4):
    card.insert(s, [])
    for r in range(13):
        card[s].insert(r, 0)

for c in range(n):
    s, r = stdin.readline().split(' ')
    r = int(r) - 1
    card[smap[s]][r] = 1

for s in range(4):
    for r in range(13):
        if card[s][r] == 0:
            print(rsmap[s], r + 1)