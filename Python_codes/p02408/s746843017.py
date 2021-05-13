n = input()

S = [[0 for j in xrange(13)] for i in xrange(4)]
    
for i in xrange(n):
    tmp1, tmp2 = map(str, raw_input().split())
    if tmp1 == "S":
        S[0][int(tmp2) - 1] = 1
    elif tmp1 == "H":
        S[1][int(tmp2) - 1] = 1
    elif tmp1 == "C":
        S[2][int(tmp2) - 1] = 1
    elif tmp1 == "D":
        S[3][int(tmp2) - 1] = 1
        
for i in xrange(4):
    for j in xrange(13):
        if S[i][j] == 0:
            if i == 0:
                print "S",
            elif i == 1:
                print "H",
            elif i == 2:
                print "C",
            elif i == 3:
                print "D",
            print "%d" % (j + 1)