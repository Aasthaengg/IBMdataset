n = int(raw_input())

list_cards = [0 for i in range(53)]

for i in range(1, n + 1):
    Type, Number = raw_input().split()
    Number = int(Number)
    if Type == "S":
        x = 0
    elif Type == "H":
        x = 1
    elif Type == "C":
        x = 2
    elif Type == "D":
        x = 3
    list_cards[x * 13 + Number] = 1
    
for i in range(1, 53):
    if list_cards[i] == 0:
        if 0 < i and i < 14:
            Type = "S"
        elif 13 < i and i < 27:
            Type = "H"
        elif 26 < i and i < 40:
            Type = "C"
        elif 39 < i and i < 53:
            Type = "D"
    
        d = i % 13
        if d == 0:
            d = 13
        if Type == "S":
            print "S %d" %(d)
        elif Type == "H":
            print "H %d" %(d)
        elif Type == "C":
            print "C %d" %(d)
        elif Type == "D":
            print "D %d" %(d)