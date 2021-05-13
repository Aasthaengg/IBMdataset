S = [0] * 13
H = [0] * 13
C = [0] * 13
D = [0] * 13

SUIT = {}
SUIT['S'] = S
SUIT['H'] = H
SUIT['C'] = C
SUIT['D'] = D

n = input()
for _ in xrange(n):
    line = raw_input().split()
    (SUIT[line[0]])[int(line[1]) - 1] = 1

for suit in ['S', 'H', 'C', 'D']:
    for i in xrange(13):
        if (SUIT[suit])[i] == 0:
            print '%s %d' % (suit, i + 1)