deck = [[0] * 13 for i in range(4)]
n = input()

for i in range(0, n) :
    suit, num = raw_input().split(" ")
    if (suit == "S") :
        deck[0][int(num)-1] = 1
    if (suit == "H") :
        deck[1][int(num)-1] = 1
    if (suit == "C") :
        deck[2][int(num)-1] = 1
    if (suit == "D") :
        deck[3][int(num)-1] = 1

for i in range(0, 4) :
    for j in range(0, 13) :
        if (deck[i][j] == 0) :
            if (i == 0) :
                print("S %s" % str(j+1))
            if (i == 1) :
                print("H %s" % str(j+1))
            if (i == 2) :
                print("C %s" % str(j+1))
            if (i == 3) :
                print("D %s" % str(j+1))