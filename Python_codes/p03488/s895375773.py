S = input().split('T')
x, y = map(int, input().split())

X = []
Y = []
for i, s in enumerate(S):
    if i % 2 == 0:
        X.append(len(s))
    else:
        Y.append(len(s))

if sum(X) < abs(x) or sum(Y) < abs(y):
    print('No')
    exit()

pos = set([X[0]])
for i in range(1, len(X)):
    d = X[i]
    npos = set()
    for p in pos:
        npos.add(p + d)
        npos.add(p - d)
    pos = npos
flag_x = x in pos

pos = set([0])
for i in range(len(Y)):
    d = Y[i]
    npos = set()
    for p in pos:
        npos.add(p + d)
        npos.add(p - d)
    pos = npos
flag_y = y in pos

if flag_x and flag_y:
    print('Yes')
else:
    print('No')
