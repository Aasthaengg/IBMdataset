n = input()
S = []
H = []
C = []
D = []
i = 1
while True:
    if i > n:
        break

    card = raw_input().split()
    mark = card[0]
    num = int(card[1])

    if mark == 'S':
        S.append(num)
    elif mark == 'H':
        H.append(num)
    elif mark == 'C':
        C.append(num)
    elif mark == 'D':
        D.append(num)

    i += 1

diff_S = set(range(1, 14)) - set(S)
for s in sorted(diff_S):
    print "S %d" % s
diff_H = set(range(1, 14)) - set(H)
for h in sorted(diff_H):
    print "H %d" % h
diff_C = set(range(1, 14)) - set(C)
for c in sorted(diff_C):
    print "C %d" % c
diff_D = set(range(1, 14)) - set(D)
for d in sorted(diff_D):
    print "D %d" % d