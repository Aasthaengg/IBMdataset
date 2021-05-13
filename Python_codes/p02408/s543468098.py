n = int(input())
Cards = [[0 for i in range(13)]  for j in range(4)]

for i in range(n):
    Mark,Number = input().split()
    if Mark == "S":
        Cards[0][int(Number) - 1] = 1
    elif Mark == "H":
        Cards[1][int(Number) - 1] = 1
    elif Mark == "C":
        Cards[2][int(Number) - 1] = 1
    elif Mark == "D":
        Cards[3][int(Number) - 1] = 1

for x in range(4):
    for y in range(13):
        if Cards[x][y] == 0:
            if x == 0:
                print("S",y+1)
            elif x == 1:
                print("H",y+1)
            elif x == 2:
                print("C", y + 1)
            elif x == 3:
                print("D", y + 1)