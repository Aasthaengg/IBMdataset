c=[]
for i in range(3):
    c.append(list(map(int,input().split())))
for i in range(2):
    if c[i+1][0]-c[i][0]==c[i+1][1]-c[i][1] and c[i+1][1]-c[i][1]==c[i+1][2]-c[i][2] and c[0][i+1]-c[0][i]==c[1][i+1]-c[1][i] and c[1][i+1]-c[1][i]==c[2][i+1]-c[2][i]:
        flg=0
    else:
        flg=1
if flg==0:
    print("Yes")
else:
    print("No")
