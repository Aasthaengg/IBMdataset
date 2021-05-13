n, m, l = map(int, input().split())

mathlist1 = [list(map(int, input().split())) for x in range(n)]
mathlist2 = [list(map(int, input().split())) for y in range(m)]
mathlist3 = list(map(list, zip(*mathlist2)))
mathlist4 = []

for d in mathlist1:
    interim = []
    for e in mathlist3:
        result = 0
        for f, g in zip(d, e):
            result += f * g
        interim.append(result)
    mathlist4.append(interim)

for h in mathlist4:
    print(*h, sep=' ')

