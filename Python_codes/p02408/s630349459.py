n = int(input())

cards = [[False for i in range(13)] for j in range(4)]

for i in range(n):
    n,m = input().split()
    m = int(m)
    if n == 'S':
        cards[0][m-1] = True
    elif n == 'H':
        cards[1][m-1] = True
    elif n == 'C':
        cards[2][m-1] = True
    elif n == 'D':
        cards[3][m-1] = True
for j in range(4):
    for i in range(13):
        if cards[j][i] == False:
            if j == 0:
                print('S ' + str(i+1))
            elif j == 1:
                print('H ' + str(i+1))
            elif j == 2:
                print('C ' + str(i+1))
            elif j == 3:
                print('D ' + str(i+1))