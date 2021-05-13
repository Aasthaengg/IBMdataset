r, c = map(int, input().split())
mathlist = []
for x in range(r):
    mathlist.append(list(map(int, input().split())))

mathlist_change = list(map(list, zip(*mathlist)))
mathlist_last = 0

for y in mathlist:
    for z in y:
        print('{a} '.format(a=z), end='')
    print(sum(y))

for i in mathlist_change:
    print('{b} '.format(b=sum(i)), end='')
    mathlist_last += sum(i)

print(mathlist_last)

