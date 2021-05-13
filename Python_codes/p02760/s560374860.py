d=[[int(s) for s in input().split()] for i in range(3)]
N=int(input())
B=[int(input()) for i in range(N)]
for i in range(len(B)):
    for j in range(3):
        for k in range(3):
            if B[i]==d[j][k]:
                d[j][k]=-1
x=0
for i in range(3):
    if d[i][0]==d[i][1]==d[i][2]==-1 or d[0][i]==d[1][i]==d[2][i]==-1:
        x+=1
        print("Yes")
        break
if x==0:
    if d[0][0]==d[1][1]==d[2][2]==-1 or d[0][2]==d[1][1]==d[2][0]==-1:
        print("Yes")
    else:
        print("No")