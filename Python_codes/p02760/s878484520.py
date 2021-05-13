ls=[]
for i in range(3):
    ls1=list(map(int,input().split()))
    ls.append(list(ls1))
    ls1.clear()
#print(ls)
N=int(input())
for i in range(N):
    b = int(input())
    for j in range(3):
        for l in range(3):
            if ls[l][j] == b:
                ls[l][j] = -1
flg = False
for i in range(3):
    if ls[i][0] == ls[i][1] == ls[i][2] == -1:
        print("Yes")
        flg = True
        break
    elif ls[0][i] == ls[1][i] == ls[2][i] == -1:
        print("Yes")
        flg = True
        break
    elif ls[0][0] == ls[1][1] == ls[2][2] == -1:
        print("Yes")
        flg = True
        break
    elif ls[0][2] == ls[1][1] == ls[2][0] == -1:
        print("Yes")
        flg = True
        break
if flg == False:
    print("No")
