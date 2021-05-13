n = input()

data = {
    'S':[0 for x in range(13)],
    'H':[0 for x in range(13)],
    'C':[0 for x in range(13)],
    'D':[0 for x in range(13)]
}

for i in range(n):
    s,num = raw_input().split()
    data[s][int(num)-1] = 1

for a in['S','H','C','D']:
    for b in range(13):
        if data[a][b] == 0:
            print('{0} {1}'.format(a,b+1))