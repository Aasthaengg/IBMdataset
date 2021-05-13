I = input().split()
r = int(I[0])
c = int(I[1])
Rsum = 0
Csum = (c + 1) * [0]

o = [[0 for i2 in range(c + 1)] for i1 in range(r + 1)]

for i in range(r + 1):
    if i < r:
        Irc = input().split()
    for j in range(c):
        if i < r:
            o[i][j] = int(Irc[j])
            Rsum += o[i][j]
            Csum[j] += o[i][j]
        else:
            o[i][j] += Csum[j]
            Rsum += o[i][j]
    o[i][c] = Rsum
    Csum[c] = o[i][c]
    Rsum = 0

for i in range(r + 1):
    for j in range(c + 1):
        print(str(o[i][j]), end = '')
        if j != c:
            print(' ', end = '')
    print()