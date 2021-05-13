bingo=[]
for i in range(3):
    array=map(int,input().split())
    bingo.append(list(array))

N=int(input())
b=[]
for i in range(N):
    b.append(int(input()))

for i in range(3):
    for j in range(3):
        for k in b:
            if bingo[i][j]==k:
                bingo[i][j]=-1

flg=False
for i in range(3):
    if bingo[i][0]==-1 and bingo[i][1]==-1 and bingo[i][2]==-1:
        flg=True
        break
    if bingo[0][i]==-1 and bingo[1][i]==-1 and bingo[2][i]==-1:
        flg=True
        break

if bingo[0][0]==-1 and bingo[1][1]==-1 and bingo[2][2]==-1:
    flg=True
elif bingo[0][2]==-1 and bingo[1][1]==-1 and bingo[2][0]==-1:
    flg=True

if flg:
    print("Yes")
else:
    print("No")