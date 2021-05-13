cards = [[False for j in range(13)] for i in range(4)]
pattern = ["S", "H", "C", "D"]
numbers = int(input())
for a in range(numbers):
    ch,rank = input().split()
    rank = int(rank)
    if ch == "S":
        cards[0][rank-1] = True
    elif ch == "H":
        cards[1][rank-1] = True
    elif ch == "C":
        cards[2][rank-1] = True
    elif ch == "D":
        cards[3][rank-1] = True

for i in range(4):
    for j in range(13):
        if cards[i][j] == False:
            print(pattern[i],j+1)
