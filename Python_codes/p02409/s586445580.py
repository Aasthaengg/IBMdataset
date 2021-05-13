n = int(raw_input())

D = []
for i in range(0,4):
    bb = []
    for k in range(0,3):
        b = [0,0,0,0,0,0,0,0,0,0]
        bb.append(b)
    D.append(bb)

for i in range(0,n):
    [b,f,r,v] = raw_input().split()
    b = int(b) - 1
    f = int(f) - 1
    r = int(r) - 1
    v = int(v)
    D[b][f][r] = D[b][f][r] + v

for b in range(0,4):
    for f in range(0,3):
        s = ''
        for r in range(0,10):
            v = str(D[b][f][r])
            s = s + ' ' + v
        print s
    if b < 3:
        print "####################"