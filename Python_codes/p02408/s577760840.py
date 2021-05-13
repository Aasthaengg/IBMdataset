from sys import stdin

order = { "S" : 0, "H" : 1, "C" : 2, "D" : 3 }
cards = [
    [False] * 13, # S
    [False] * 13, # H
    [False] * 13, # C
    [False] * 13  # D
]

stdin.readline().rstrip()
while True:
    try:
        suit, num = stdin.readline().rstrip().split()
        cards[order[suit]][int(num)-1] = True
    except:
        break

order = {v:k for k, v in order.items()}
for i in range(4):
    for j in range(13):
        if cards[i][j] != True:
            print(order[i], j+1)
