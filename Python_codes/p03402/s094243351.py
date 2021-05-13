A,B = map(int,input().split())
A -= 1
B -= 1
K = 50
print(100,100)
grid1 = [['#']*100 for i in range(50)]
grid2 = [['.']*100 for i in range(50)]
for r in range(0,50,2):
    for c in range(0,100,2):
        if A > 0:
            grid1[r][c] = '.'
            A -= 1
        else:
            break

for r in range(1,50,2):
    for c in range(0,100,2):
        if B > 0:
            grid2[r][c] = '#'
            B -= 1
        else:
            break
for row in grid1:
    print(''.join(row))

for row in grid2:
    print(''.join(row))

