A = []
for i in range(3):
    A.append(list(map(int, input().split())))

N = int(input())

B = []

for i in range(N):
    B.append(int(input()))

bingo = False

#check rows and columns
for i in range(3):
    rowMatches = 0
    colMatches = 0
    for j in range(3):
        if A[i][j] in B:
            rowMatches += 1
        if A[j][i] in B:
            colMatches += 1

    if (rowMatches == 3 or colMatches == 3):
        bingo = True
        break

if (bingo):
    print("Yes")
else:
    #check diagonals
    diag1 = 0
    diag2 = 0
    for i in range(3):
        if A[i][i] in B:
            diag1 += 1
        if A[i][3-1-i] in B:
            diag2 += 1

    if (diag1 == 3 or diag2 == 3):
        print("Yes")
    else:
        print("No")