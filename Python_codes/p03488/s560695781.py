s = [len(x) for x in input().split('T')]
x, y = map(int, input().split())

X = set([s[0]])
Y = set([0])

for dx in s[2::2]:
    tX = set()
    for Xi in X:
        tX.add(Xi-dx)
        tX.add(Xi+dx)
    X = tX

for dy in s[1::2]:
    tY = set()
    for Yi in Y:
        tY.add(Yi-dy)
        tY.add(Yi+dy)
    Y = tY

if x in X and y in Y:
    print('Yes')
else:
    print('No')
