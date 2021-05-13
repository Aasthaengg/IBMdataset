Card = [list(map(int, input().split())) for _ in range(3)]
Bingo = [[False]*3 for _ in range(3)]
N = int(input())
for i in range(N):
    b = int(input())
    for j in range(3):
        if b in Card[j]:
            Bingo[j][Card[j].index(b)] = True
ans = False
for i in range(3):
    if all(Bingo[i][j] for j in range(3)):
        ans = True

for j in range(3):
    if Bingo[0][j] and Bingo[1][j] and Bingo[2][j]:
        ans = True

if Bingo[0][0] and Bingo[1][1] and Bingo[2][2]:
    ans = True
if Bingo[0][2] and Bingo[1][1] and Bingo[2][0]:
    ans = True

if ans:
    print('Yes')
else:
    print('No')
