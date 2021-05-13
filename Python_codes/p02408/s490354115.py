t = int(raw_input())

D = []
for i in range(0,4):
    base = [0,0,0,0,0,0,0,0,0,0,0,0,0] 
    D.append(base)
M = ['S','H','C','D']
for i in range(0,t):
    [m,v] = raw_input().split()
    v = int(v) - 1
    if m == 'S':
        D[0][v] = 1
    if m == 'H':
        D[1][v] = 1
    if m == 'C':
        D[2][v] = 1
    if m == 'D':
        D[3][v] = 1

for y in range(0,4):
    for x in range(0,13):
        if D[y][x] == 0:
            print M[y],x+1