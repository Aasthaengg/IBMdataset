h,w = map(int,input().split())
aij = [[int(i) for i in input().split()] for j in range(h)]

move = []

"""
for i in range(w-1,-1,-1):
    print(i)
""" 
 
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if aij[i][j] % 2 == 1:
                if j == w-1:
                    if i == h-1:
                        break
                    move.append([[i+1,j+1],[i+1+1,j+1]])
                    aij[i+1][j] += 1
                else:
                    move.append([[i+1,j+1],[i+1,j+1+1]])
                    aij[i][j+1] += 1
    else:
        for j in range(w-1,-1,-1):
            if aij[i][j] % 2 == 1:
                if j == 0:
                    if i == h-1:
                        break
                    move.append([[i+1,j+1],[i+1+1,j+1]])
                    aij[i+1][j] += 1
                else:
                    move.append([[i+1,j+1],[i+1,j+1-1]])
                    aij[i][j-1] += 1


print(len(move))

for i in range(len(move)):
    for j in range(len(move[i])):
        print(*move[i][j],end='')
        if j == 1:
            continue
        print(end=' ')
    print()