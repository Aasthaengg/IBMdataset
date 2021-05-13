n = int(raw_input())
S = [0 for i in range(13)]
H = [0 for i in range(13)]
C = [0 for i in range(13)]
D = [0 for i in range(13)]

for i in range(n):
    card = str(raw_input())
    if card[0] == 'S':
        for j in range(13):
            if str(j+1) == card[2:len(card)]:
                S[j] = 1
    elif card[0] == 'H':
        card.replace("H ", "")
        for j in range(13):
            if str(j+1) == card[2:len(card)]:
                H[j] = 1
    elif card[0] == 'C':
        card.replace("C ", "")
        for j in range(13):
            if str(j+1) == card[2:len(card)]:
                C[j] = 1
    elif card[0] == 'D':
        card.replace("D ", "")
        for j in range(13):
            if str(j+1) == card[2:len(card)]:
                D[j] = 1
                
for i in range(13):
    if S[i] == 0:
        print "S %d" % (i+1)
for i in range(13):
    if H[i] == 0:
        print "H %d" % (i+1)
for i in range(13):
    if C[i] == 0:
        print "C %d" % (i+1)
for i in range(13):
    if D[i] == 0:
        print "D %d" % (i+1)