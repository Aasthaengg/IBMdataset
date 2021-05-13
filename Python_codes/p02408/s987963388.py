N = int(input())

cards = [[0 for i in range(13)] for j in range(4)]

for num in range(N):
    i = list(map(str, input().split()))
    if i[0] == 'S':
        cards[0][int(i[1])-1] = 1
    elif i[0] == 'H':
        cards[1][int(i[1])-1] = 1
    elif i[0] == 'C':
        cards[2][int(i[1])-1] = 1
    elif i[0] == 'D':
        cards[3][int(i[1])-1] = 1

for j in range(4):
    for k in range(13):
        if cards[j][k] == 0:
            if j == 0:
                print('S', k+1)
            elif j == 1:
                print('H', k+1)
            elif j == 2:
                print('C', k+1)
            elif j == 3:
                print('D', k+1)
