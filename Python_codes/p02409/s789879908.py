import sys

S = [[[0 for k in xrange(10)] for j in xrange(3)] for i in xrange(4)]

n = input()

for l in xrange(n):
    b, f, r, v = map(int, raw_input().split())
    S[b - 1][f - 1][r - 1] += v
    
for k in xrange(4):
    for j in xrange(3):
        for i in xrange(10):
            tmp = ' ' + str(S[k][j][i]) 
            sys.stdout.write(tmp)
        print ""
    if k != 3:
        print "#" * 20