A = [None]*3
for i in range(3):
    A[i] = list(map(int, input().split()))

bingocard = [[0]*4 for _ in range(4)]
N = int(input())
for _ in range(N):
    b = int(input())
    for row in range(3):
        for col in range(3):
            if b == A[row][col]:
                bingocard[row][col] = 1
                bingocard[row][3] += 1
                bingocard[3][col] += 1

flag = False
#横
for row in bingocard:
    if row[3] == 3:
        flag = True

#縦
for col in bingocard[3]:
    if col == 3:
        flag = True
    
#斜め
if bingocard[0][0] + bingocard[1][1] + bingocard[2][2] == 3:
    flag = True
if bingocard[2][0] + bingocard[1][1] + bingocard[0][2] == 3:
    flag = True

if flag:
    print('Yes')
else:
    print('No')