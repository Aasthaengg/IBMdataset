def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

ar=[]
for i in range(3):
    ar.append(lis())
mark=[[0]*3 for _ in range(3)]
n=int(input())
for _ in range(n):
    k=int(input())
    for i in range(3):
        for j  in range(3):
            if ar[i][j]==k:
                mark[i][j]=1

for i in range(3):
    if mark[i][1]==mark[i][2]==mark[i][0]==1:
        print("Yes")
        quit()
for i in range(3):
    if mark[1][i]==mark[2][i]==mark[0][i]==1:
        print("Yes")
        quit()
if mark[0][0]==mark[1][1]==mark[2][2]==1:
    print("Yes")
    quit()
if mark[0][2]==mark[1][1]==mark[2][0]==1:
    print("Yes")
    quit()
print("No")


