cards = {
'S':[0 for i in range(13)],
'H':[0 for i in range(13)],
'C':[0 for i in range(13)],
'D':[0 for i in range(13)]
}
n = int(input())
for i in range(n):
    c, s = input().split()
    cards[c][int(s)-1] = int(s)
for i in ('S','H','C','D'):
    for j in range(13):
        if cards[i][j] == 0:
            print('{} {}'.format(i,j+1))